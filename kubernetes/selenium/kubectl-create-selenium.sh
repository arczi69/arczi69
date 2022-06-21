#/bin/bash
kubectl create namespace creds-tools
kubectl label namespace creds-tools istio-injection=enabled
kubectl apply -f selenium-hub-deployment.yaml
kubectl apply -f selenium-node-chrome-deployment.yaml
kubectl apply -f selenium-hub-gateway.yaml
