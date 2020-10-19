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
sh scripts/setup_kubeless.sh
kubectl apply -f mongo-deployment.yaml
kubectl apply -f mongo-service.yaml
```

## deploy new kubeless function

```sh
sh scripts/deploy.sh
```

## update existing kubeless function

```sh
sh scripts/update.sh
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

## install kubeless client

```sh
curl -OL https://github.com/kubeless/kubeless/releases/download/v1.0.7/kubeless_darwin-amd64.zip && \
  unzip kubeless_darwin-amd64.zip && \
  sudo mv bundles/kubeless_darwin-amd64/kubeless /usr/local/bin/
```

## call function with client

```sh
kubeless function call get-event
kubeless function call put-event --data ''
```
