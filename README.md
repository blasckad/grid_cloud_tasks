# Task 1: Docker Two-Container System with SQLite

## System Components

- **Container 1 (db)** — Hosts a SQLite database.
- **Container 2 (app)** — A Flask API that connects to the database and provides an HTTP interface.

## Key Features

- Uses a shared volume to persist SQLite data even when containers are restarted.
- The Flask app automatically creates a table and inserts a test record on first run.
- Accessing `http://localhost:5000/` returns the contents of the `users` table.

## Getting Started

```bash
docker-compose up --build
```

# Task2: Kubernetes Backend-Frontend System

## Overview

This project demonstrates a simple **microservice setup** using Kubernetes, consisting of a replicated backend and a frontend with external access.

## Components

- **Backend**
  - Python Flask app that responds to HTTP GET requests
  - Replicated with a Kubernetes `Deployment` (3 replicas)
  - Exposed internally via `ClusterIP` `Service`

- **Frontend**
  - Python Flask app that sends requests to the backend
  - Exposed externally via `LoadBalancer` `Service`
  - Routes responses from backend to users

## Kubernetes Resources

- `backend/k8s/deployment.yaml` – Backend deployment with 3 pods
- `backend/k8s/service.yaml` – Internal ClusterIP service
- `frontend/k8s/deployment.yaml` – Frontend deployment
- `frontend/k8s/service.yaml` – External LoadBalancer service

## Workflow

1. User sends request to **frontend-service**
2. Frontend makes HTTP call to **backend-service**
3. Backend responds, frontend formats the result
4. User receives the message:  
   `Frontend received: Hello from the backend!`

## Testing

```bash
kubectl apply -f backend/k8s/
kubectl apply -f frontend/k8s/
curl http://<frontend-external-ip>/
```
