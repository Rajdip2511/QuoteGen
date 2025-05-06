# QuoteGen - Scalable Web Application with Full DevOps Pipeline

## Repository Information
- GitHub Repository: https://github.com/Rajdip2511/QuoteGen.git
- Clone URL: `https://github.com/Rajdip2511/QuoteGen.git`

## Project Overview
This project implements a scalable web application with a complete DevOps pipeline, incorporating:
- Version control with Git
- CI/CD pipeline using Jenkins
- Configuration management with Ansible
- Container orchestration using Kubernetes
- Monitoring and logging with Prometheus, Grafana, and ELK Stack

## Architecture
- Frontend: React.js application
- Backend: flask/python
- Container Runtime: Docker
- Orchestration: Kubernetes
- Monitoring: Prometheus + Grafana
- Logging: ELK Stack
- ci/cd : jenkins
- codeDeployment: Github
## Directory Structure
```
QuoteGen/
├── frontend/           # React.js frontend application
├── backend/           # Node.js backend API
├── kubernetes/        # Kubernetes manifests
├── ansible/          # Ansible playbooks
├── monitoring/       # Monitoring configurations
│   ├── prometheus/   # Prometheus configs
│   ├── grafana/      # Grafana dashboards
│   └── elk/          # ELK Stack setup
├── Jenkinsfile       # CI/CD pipeline definition
└── docker-compose.yml # Local development setup
```

## Setup Instructions

### Prerequisites
- Docker
- Kubernetes cluster
- Jenkins
- Ansible
- Node.js
- npm

### Local Development
1. Clone the repository:
   ```bash
   git clone https://github.com/Rajdip2511/QuoteGen.git
   ```

2. Start local development environment:
   ```bash
   docker-compose up
   ```

### Production Deployment
1. Configure Jenkins credentials
2. Set up Kubernetes cluster
3. Deploy using Jenkins pipeline:
   - Push to main branch
   - Jenkins will automatically build and deploy

## Monitoring Setup
- Prometheus: http://[your-domain]:9090
- Grafana: http://[your-domain]:3000
- Kibana: http://[your-domain]:5601

## Security Considerations
- HTTPS enabled
- Container security policies
- Network policies
- Resource limits
- Non-root container execution

## Contributing
1. Fork the repository
2. Create feature branch
3. Submit pull request

## License
MIT License - See LICENSE file for details 