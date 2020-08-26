#!/bin/bash

DATA_PATH_1=data/F01705150050.json
DATA_PATH_2=data/F01705150090.json

curl -k -L -H "Content-Type: application/json" \
  https://localhost:6443/api/v1/namespaces/default/services/put-event:http-function-port/proxy/ \
  -d @$DATA_PATH_1

echo \\n

curl -k -L -H "Content-Type: application/json" \
  https://localhost:6443/api/v1/namespaces/default/services/put-event:http-function-port/proxy/ \
  -d @$DATA_PATH_2

echo \\n
