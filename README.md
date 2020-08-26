# kind-kubeless

## install kubernetes in docker

```sh
brew install kind
```

## install mongodb client

```sh
brew tap mongodb/brew
brew install mongodb-community-shell
```

## clear up space for kind

```sh
docker system prune
docker rmi $(docker image ls -a -q)
```

## deploy kind cluster

```sh
kind create cluster --config kind-config.yaml
kind get kubeconfig > ~/.kube/configs/kind-kind
kubectl config current-context
```

## deploy kubeless and mongodb to kind cluster

```sh
KUBECONFIG=~/.kube/configs/kind-kind sh scripts/setup_kubeless.sh
KUBECONFIG=~/.kube/configs/kind-kind kubectl apply -f mongo-deployment.yaml
KUBECONFIG=~/.kube/configs/kind-kind kubectl apply -f mongo-service.yaml
```

## deploy new kubeless function

```sh
KUBECONFIG=~/.kube/configs/kind-kind sh scripts/deploy.sh
```

## update existing kubeless function

```sh
KUBECONFIG=~/.kube/configs/kind-kind sh scripts/update.sh
```

## give anonymous users the cluster-admin role

```sh
kubectl create clusterrolebinding --user system:anonymous cluster-anon --clusterrole cluster-admin
```

## call put function with curl script

```sh
sh scripts/upload_data.sh

data inserted successfully with id: 5f45e104fb7f497571a4113b
...
```

## call get function from web browser

https://127.0.0.1:6443/api/v1/namespaces/default/services/get-event:http-function-port/proxy/?id=5f45e104fb7f497571a4113b
