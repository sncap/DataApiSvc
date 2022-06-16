INSERT INTO public.data_service (name, api_url, sql, result_max_cnt, result_timeout, cache_timeout) VALUES ('ds2', 'api/v2/demo_sleep_sql', 'select 1 from pg_sleep(4)', -1, 3, 3);
INSERT INTO public.data_service (name, api_url, sql, result_max_cnt, result_timeout, cache_timeout) VALUES ('ds2', 'api/v2/demo_users', '/* api/v2/demo_users */
SELECT user_id, name, password, role, use_yn, email
FROM demo_users 
WHERE name like :name ', 3, -1, 3);
INSERT INTO public.data_service (name, api_url, sql, result_max_cnt, result_timeout, cache_timeout) VALUES ('ds1', 'api/v2/listallds', 'select  * from data_source', -1, -1, 0);
INSERT INTO public.data_service (name, api_url, sql, result_max_cnt, result_timeout, cache_timeout) VALUES ('ds1', 'api/v2/listallsql', 'select  * from data_service', -1, -1, 0);
INSERT INTO public.data_service (name, api_url, sql, result_max_cnt, result_timeout, cache_timeout) VALUES ('ds1', 'api/v2/updateds', 'INSERT INTO data_source
(name, db_url, conn_max_cnt, conn_timeout, update_time, update_user, biz_dept, biz_name)
VALUES(:name, :db_url, :conn_max_cnt, :conn_timeout, now(), :update_user, :biz_dept, :biz_name)
ON CONFLICT (name)
DO UPDATE SET db_url = :db_url,  conn_max_cnt  = :conn_max_cnt,  conn_timeout =:conn_timeout ,
update_time = now() , update_user=:update_user , biz_dept=:biz_dept , biz_name=:biz_name
', -1, -1, 0);
INSERT INTO public.data_service (name, api_url, sql, result_max_cnt, result_timeout, cache_timeout) VALUES ('ds1', 'api/v2/updatesql', 'INSERT INTO data_service
(name, api_url, sql, result_max_cnt, result_timeout)
VALUES(:name, :api_url, :sql, :result_max_cnt, :result_timeout)
ON CONFLICT (api_url)
DO UPDATE SET name = :name,  sql  = :sql,  result_max_cnt =:result_max_cnt ,
result_timeout=:result_timeout

/* INSERT INTO data_service
(name, api_url, sql, result_max_cnt, result_timeout)
VALUES(:name, :api_url, :sql, :result_max_cnt, :result_timeout)
*/', -1, -1, 0);
INSERT INTO public.data_service (name, api_url, sql, result_max_cnt, result_timeout, cache_timeout) VALUES ('ds1', 'capi/v2/demo_users', 'select * from demo_users where name like :name', -1, -1, 0);