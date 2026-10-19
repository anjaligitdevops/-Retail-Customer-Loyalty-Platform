# Retail Customer Loyalty & Promotions Platform

## Project Overview
A Flask-based REST API application for a retail loyalty platform. It provides customer loyalty points and promotional offers. This project is being developed as a hands-on learning project for Azure DevOps, CI/CD, and cloud deployment.

## Features
- **Home API (`/`)** — Returns application status.
- **Loyalty API (`/loyalty`)** — Returns sample customer loyalty points.
- **Promotions API (`/promotions`)** — Returns promotional offers and discounts.
- **Automated Testing** — Uses pytest to validate API responses and status codes.

## Technology Stack
- Python 3.10
- Flask
- pytest
- Git and GitHub
- Azure DevOps CI/CD — planned
- Docker, Terraform, Azure Container Registry (ACR), and Azure Kubernetes Service (AKS) — planned

## Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/anjaligitdevops/-Retail-Customer-Loyalty-Platform.git
cd -Retail-Customer-Loyalty-Platform
```

### 2. Create and activate a virtual environment
On Windows PowerShell:
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies
```bash
python -m pip install -r requirements.txt
python -m pip install pytest
```

### 4. Start the application
```bash
python app.py
```

### 5. Access the APIs
- Home: `http://127.0.0.1:5000/`
- Loyalty: `http://127.0.0.1:5000/loyalty`
- Promotions: `http://127.0.0.1:5000/promotions`

### 6. Run automated tests
```bash
python -m pytest -v
```

Expected result: **3 tests passed**.

## Project Roadmap
1. Build and test Flask REST APIs.
2. Set up a CI pipeline using Azure DevOps YAML.
3. Build and containerize the application with Docker.
4. Push the Docker image to Azure Container Registry.
5. Provision Azure infrastructure using Terraform.
6. Deploy the application to Azure Kubernetes Service (AKS).

## Author
Anjali Rai

GitHub: [anjaligitdevops](https://github.com/anjaligitdevops)
