docker run -d --rm --name my_redis -p 6379:6379 redis:5.0-alpine

docker run -d --rm --name my_postgres -e POSTGRES_PASSWORD=password -e POSTGRES_USER=admin -e POSTGRES_DB=das_db -p 5432:5432 -v /data/postgres/data:/var/lib/postgresql/data:rw postgres:13

