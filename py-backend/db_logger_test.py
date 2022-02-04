'''
CREATE TABLE log (
    id SERIAL8 PRIMARY KEY,
    log_level int NULL,
    log_levelname char(32) NULL,
    log string NOT NULL,
    created_at timestamp  NOT NULL,
    created_by char(256) NOT NULL
)
'''
import logging
class LogDBHandler(logging.Handler):
    '''
    Customized logging handler that puts logs to the database.
    pymssql required
    '''
    def __init__(self, sql_conn, sql_cursor, db_tbl_log):
        logging.Handler.__init__(self)
        self.sql_cursor = sql_cursor
        self.sql_conn = sql_conn
        self.db_tbl_log = db_tbl_log

    def emit(self, record):
        # Set current time
        tm = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(record.created))
        # Clear the log message so it can be put to db via sql (escape quotes)
        self.log_msg = record.msg
        self.log_msg = self.log_msg.strip()
        self.log_msg = self.log_msg.replace('\'', '\'\'')
        # Make the SQL insert
        sql = 'INSERT INTO ' + self.db_tbl_log + ' (log_level, ' + \
            'log_levelname, log, created_at, created_by) ' + \
            'VALUES (' + \
            ''   + str(record.levelno) + ', ' + \
            '\'' + str(record.levelname) + '\', ' + \
            '\'' + str(self.log_msg) + '\', ' + \
            '\'' + tm + '\'::timestamp , ' + \
            '\'' + str(record.name) + '\')'
        try:
            self.sql_cursor.execute(sql)
            self.sql_conn.commit()
        # If error - print it out on screen. Since DB is not working - there's
        # no point making a log about it to the database :)
        except:
            print (sql)
            print ('CRITICAL DB ERROR! Logging to database not possible!')


import psycopg2
import time
import logging

db_server = 'db.wdplatform.com'
db_user = 'maxroach'
db_password = ''
db_dbname = 'yebb'
db_tbl_log = 'log'
log_file_path = './test_log.txt'
log_error_level     = 'DEBUG'       # LOG error level (file)

log_to_db = True                    # LOG to database?


# Main settings for the database logging use
if (log_to_db):
    # Make the connection to database for the logger
    log_conn = psycopg2.connect( database='yebb',
        user='maxroach',
        sslmode='disable',
        port=26257,
        host='db.wdplatform.com')

    #log_conn = psycopg2.connect(db_server, db_user, db_password, db_dbname, 30)
    log_cursor = log_conn.cursor()
    logdb = LogDBHandler(log_conn, log_cursor, db_tbl_log)

# Set logger
logging.basicConfig(filename=log_file_path)

# Set db handler for root logger
if (log_to_db):
    logging.getLogger('').addHandler(logdb)
# Register MY_LOGGER
log = logging.getLogger('MY_LOGGER')
log.setLevel(log_error_level)
# Example variable
test_var = 'This is test message'

# Log the variable contents as an error
for i in range(100):
    log.error('This error occurred: %s' % test_var)