import datetime
import decimal
import json
import sqlalchemy
#import airspeed
from flask import Flask, request
from sqlalchemy.pool import QueuePool
from sqlalchemy.sql import text
from flask_caching import Cache

import logging
# disble flask log
#logger = logging.getLogger('werkzeug')
#logger.setLevel(logging.INFO)

ds_info = []


# log format
logging.basicConfig(level=logging.DEBUG, format="[%(asctime)s:%(filename)s:%(funcName)s:%(lineno)d] %(message)s",
                    datefmt="%m/%d %H:%M:%S")
#sqlalchemylogger = logging.getLogger('sqlalchemy.engine')
#sqlalchemylogger.setLevel(logging.INFO)
logger = logging.getLogger('data_svc')
logger.setLevel(logging.INFO)
#logger.debug('[Input] %s' % id)
#logger.debug('[Output] %s' % res)

db_url = 'cockroachdb://maxroach@localhost:26257/demo?sslmode=disable'
engine = sqlalchemy.create_engine(db_url, 
                                  poolclass=QueuePool, pool_size=1, max_overflow=0, pool_timeout=3)


                                  #connect_args={'connect_timeout': 1})
#                                  connect_args={'connect_timeout':2})
print("pool size = {}".format(engine.pool.size()))
#print("max overflow  = {}".format(engine.max.overflow()))

def json_default(value):
    if isinstance(value, datetime.date):
        return value.strftime('%Y/%m/%d %H:%M:%S')
    elif isinstance(value, decimal.Decimal):
        return float(value)
    raise TypeError('not JSON serializable')

def exec(query_id, param):
    item = get_query(query_id)
    sql = item['sql']
    result_max_cnt = item['result_max_cnt']
    result_timeout = item['result_timeout']
    
    logger.debug(sql)
    logger.debug(param)
    logger.debug(result_max_cnt)
    logger.debug(result_timeout)
    #template = airspeed.Template(sql)
    #sql = template.merge(param)
    with engine.connect() as conn:
        conn.execute(text('SET statement_timeout TO %d' % (result_timeout*1000))) 
        # SET LOCK_TIMEOUT 5000; 
        # SET SESSION MAX_EXECUTION_TIME=2000;
        
        results = conn.execute(text(sql), param).fetchmany(size=result_max_cnt)
        return results

sql_data_service = text("SELECT sql,result_max_cnt,result_timeout  FROM data_service WHERE api_url = :key")
def get_query(api_url):
    with engine.connect() as con:
        results = con.execute(sql_data_service, {'key': api_url} )
        return results.fetchone()

app = Flask(__name__)
'''
config = {
    "DEBUG": True,          # some Flask specific configs
    "CACHE_TYPE": "redis", # Flask-Caching related configs
    "CACHE_REDIS_URL": 'redis://localhost:6379/0',
    "CACHE_DEFAULT_TIMEOUT": 300
}
app.config.from_mapping(config)
cache = Cache(app)
'''

@app.route('/api/<path:api_url>')
#@cache.cached(timeout=10, query_string=True)
def callapi(api_url):
    input = request.args
    logger.debug('[Input] %s' % input)
    api_url = 'api/' + api_url
    logger.debug('[api_url] %s' % api_url)
    results = exec(api_url, input)
    res = []
    for row in results:
        res.append(dict(row))
    out = json.dumps(res, default=json_default, ensure_ascii=False)
    logger.debug('[Output] %s' % out)
    return out


sql_data_source = text("SELECT db_url, conn_max_cnt, conn_timeout FROM data_source WHERE name = :key") 
def get_ds(name):
    with engine.connect() as con:
        results = con.execute(sql_data_source, {'key': name} )
        return results.fetchone()
    
@app.route('/ds_reload/<name>')
def ds_reload(name):
    item = get_ds(name)
    new_db_url = item['db_url']
    conn_max_cnt = item['conn_max_cnt']
    print(conn_max_cnt)
    conn_timeout = item['conn_timeout']
    print(conn_timeout)
    engine = sqlalchemy.create_engine(new_db_url,poolclass=QueuePool, 
                                      pool_size=conn_max_cnt, max_overflow=0, pool_timeout=conn_timeout)
    return 'reload ok'



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=False, threaded=True)
    
'''
CREATE TABLE data_service_test
(
    api_url varchar(200) NOT NULL,
    id varchar(200) NOT NULL,
    value text,
    PRIMARY KEY  ( api_url , id)
) ;

CREATE TABLE data_source
(
    name varchar(200) NOT NULL UNIQUE,
    db_url varchar(400),
    conn_max_cnt int,
    conn_timeout int,
    update_time timestamp,
    update_user varchar(200),
    biz_dept varchar(400),
    biz_name varchar(400),
    PRIMARY KEY (name)
) ;
CREATE TABLE data_service
(
    name varchar(200) ,
    api_url varchar(200) ,
    sql text,
    result_max_cnt int,
    result_timeout int,
    PRIMARY KEY (api_url)
) ;
http://localhost/api/v2/demo_users?name=%EA%B6%8C%

'''