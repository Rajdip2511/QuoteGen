#!/bin/bash

# Create monitoring namespace if it doesn't exist
kubectl create namespace monitoring --dry-run=client -o yaml | kubectl apply -f -

# Deploy Prometheus
echo "Deploying Prometheus..."
kubectl apply -f prometheus-deployment.yaml

# Deploy Grafana
echo "Deploying Grafana..."
kubectl apply -f grafana-deployment.yaml

# Create Grafana admin secret
kubectl create secret generic grafana-admin-credentials \
  --from-literal=admin-user=admin \
  --from-literal=admin-password=QuoteGen2024! \
  --namespace monitoring \
  --dry-run=client -o yaml | kubectl apply -f -

# Deploy ELK Stack
echo "Deploying ELK Stack..."
kubectl apply -f elk-stack.yaml

# Wait for pods to be ready
echo "Waiting for pods to be ready..."
kubectl wait --for=condition=ready pod -l app=prometheus -n monitoring --timeout=300s
kubectl wait --for=condition=ready pod -l app=grafana -n monitoring --timeout=300s
kubectl wait --for=condition=ready pod -l app=elasticsearch -n monitoring --timeout=300s

# Port forward for accessing services
echo "Setting up port forwarding..."
kubectl port-forward svc/prometheus -n monitoring 9090:9090 &
kubectl port-forward svc/grafana -n monitoring 3000:3000 &
kubectl port-forward svc/kibana -n monitoring 5601:5601 &

echo "
Monitoring Stack Access Information:

Prometheus:
URL: http://localhost:9090
No authentication required

Grafana:
URL: http://localhost:3000
Username: admin
Password: QuoteGen2024!

Kibana:
URL: http://localhost:5601
Username: elastic
Password: QuoteGen2024!

Please save these screenshots in the monitoring/screenshots directory:
1. Grafana Dashboard - Application Metrics
2. Grafana Dashboard - Resource Metrics
3. Prometheus Targets Page
4. Kibana Discover Page with application logs

Note: Keep this access information secure and change passwords in production.
" 