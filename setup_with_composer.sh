docker-compose stop
docker-compose rm -f
docker build ./database -t event-clickhouse
docker build ./API -t kafkapython
docker-compose up -d
docker-compose ps