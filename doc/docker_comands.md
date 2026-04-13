## Criar o container: 
```bash
docker build -t llmops-app:local .
```

## Rodar o Container: 

```bash
docker run --rm -p 8000:8000 --env-file .env llmops-app:local
```

Kubernets: 
```bash 
kubectl apply -f llmops-k8s.yaml
kubectl get pods
kubectl get svc
```

Opção 1. Rebuild com a tag que o Kubernetes espera

```bash 
docker build -t llmops-app:latest .
kubectl delete deployment llmops-app
kubectl apply -f llmops-k8s.yaml
kubectl get pods -w
```