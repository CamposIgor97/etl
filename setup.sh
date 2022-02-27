docker-compose stop
docker-compose rm -f
docker build . -t kafkapython
docker-compose up -d
docker-compose ps