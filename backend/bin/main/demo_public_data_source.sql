INSERT INTO public.data_source (name, db_url, conn_max_cnt, conn_timeout, update_time, update_user, biz_dept, biz_name, user_id, passwd, schema_name) VALUES ('ds1', 'cockroachdb://maxroach@localhost:26257/demo?sslmode=disable', 10, 4, '2020-04-29 07:29:12.506093', 'admin', 'ds', 'ds업무', null, null, null);
INSERT INTO public.data_source (name, db_url, conn_max_cnt, conn_timeout, update_time, update_user, biz_dept, biz_name, user_id, passwd, schema_name) VALUES ('ds2', 'jdbc:postgresql://localhost:26257/demo?sslmode=disable', 1, 4, '2020-04-29 07:30:08.320847', 'none', 'dept', '테스트', null, null, null);
INSERT INTO public.data_source (name, db_url, conn_max_cnt, conn_timeout, update_time, update_user, biz_dept, biz_name, user_id, passwd, schema_name) VALUES ('test2', 'mysql://test@test.com', 3, 10, '2020-04-29 07:30:22.174632', 'none', 'none', 'none', null, null, null);
INSERT INTO public.data_source (name, db_url, conn_max_cnt, conn_timeout, update_time, update_user, biz_dept, biz_name, user_id, passwd, schema_name) VALUES ('test3', 'postgre://abc@aaa.bbb.ccc/', 4, 11, '2020-04-29 07:30:39.699129', 'none', 'none', '테스트', null, null, null);
INSERT INTO public.data_source (name, db_url, conn_max_cnt, conn_timeout, update_time, update_user, biz_dept, biz_name, user_id, passwd, schema_name) VALUES ('test4', 'postgre://abc@aaa.bbb.ccc/', 4, 11, '2020-04-29 07:30:44.459375', 'none', 'none', '테스트', null, null, null);