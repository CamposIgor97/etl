minikube start
minikube docker-env
# run the command to point the VM to docker local
# below its the windows version
# & minikube -p minikube docker-env --shell powershell | Invoke-Expression

docker build ./database -t event-clickhouse
docker build ./API -t kafkapython

helm repo add bitnami https://charts.bitnami.com/bitnami
helm install my-release bitnami/kafka

helm install etl-chart etl-chart/

minikube kubectl -- get pods -A


##HELPS TO TEST
##minikube kubectl -- port-forward myapp-754c77dcff-g7k76 8080:80