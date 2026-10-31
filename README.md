# NutriPlan — Diet Planner DevOps Case Study

A student demo using Flask, HTML/CSS, Docker, Jenkins and Kubernetes.

## Features
- Takes age, height, weight, gender-for-formula, activity level and goal.
- Estimates BMI, BMR and daily calorie target.
- Displays a sample meal plan.
- Health-check endpoint: `/health`.
- Automated unit tests with pytest.

**Health note:** This is an educational demo, not medical advice or a clinical diet prescription. BMI is a limited screening measure and calorie estimates can be inaccurate for individuals. Consult a registered dietitian or healthcare professional before significant dietary changes.

## Run locally (Windows PowerShell)
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m pytest -v
python app.py
```
Open http://localhost:5000. If PowerShell blocks venv activation, skip activation and use `python -m pip install -r requirements.txt`.

## GitHub
Create an empty GitHub repository, then run in this folder (replace URL):
```powershell
git init
git add .
git commit -m "Initial Diet Planner application"
git branch -M main
git remote add origin https://github.com/YOUR_GITHUB_USERNAME/diet-planner-devops.git
git push -u origin main
```
If `origin` already exists, use `git remote set-url origin YOUR_REPOSITORY_URL`.

## Docker
Replace `DOCKERHUB_USERNAME` in `Jenkinsfile` and `deployment.yaml`.
```powershell
docker build -t YOUR_DOCKERHUB_USERNAME/diet-planner:latest .
docker login
docker push YOUR_DOCKERHUB_USERNAME/diet-planner:latest
docker run --rm -p 5000:5000 YOUR_DOCKERHUB_USERNAME/diet-planner:latest
```
Open http://localhost:5000.

## Jenkins on Windows
1. Ensure the Jenkins agent can run `python`, `docker`, `git` and `kubectl`.
2. Jenkins → Manage Jenkins → Credentials → System → Global credentials → Add Credentials.
3. Choose **Username with password**; ID must be `dockerhub-creds`. Use your Docker Hub username and a Docker Hub access token as the password (not your account password).
4. Replace `DOCKERHUB_USERNAME` in both `Jenkinsfile` and `deployment.yaml`.
5. Push the changes to GitHub.
6. Create a Pipeline job → Pipeline script from SCM → Git → repository URL → branch `*/main` → Script Path `Jenkinsfile`.
7. Click Build Now.

Pipeline stages: install dependencies → run tests → build image → Docker Hub login using Jenkins credentials → push image → deploy to Kubernetes.

**Kubernetes/Jenkins note:** Jenkins must be able to access your cluster. A Windows Jenkins service may run under a different account and may not see your personal `%USERPROFILE%\.kube\config`. If deployment fails due to kubeconfig/connection, configure cluster access for the Jenkins service account. Never commit kubeconfig secrets to GitHub.

## Kubernetes manual deployment
After replacing image name in `deployment.yaml`:
```powershell
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl get pods
kubectl get services
kubectl port-forward service/diet-planner-service 8080:5000
```
Open http://localhost:8080 and keep the port-forward terminal open. If NodePort 30190 is occupied, change it to an unused value from 30000 to 32767.

## Project structure
```text
diet-planner-devops/
├── app.py
├── planner.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
├── Jenkinsfile
├── deployment.yaml
├── service.yaml
├── README.md
├── templates/
│   ├── index.html
│   └── result.html
├── static/
│   └── style.css
└── tests/
    └── test_planner.py
```

## DevOps workflow
Developer commits code → GitHub stores source → Jenkins checks out repository → dependencies installed → pytest runs → Docker image built → image pushed to Docker Hub → Kubernetes applies deployment and service → two pods run the application and health probes check `/health`.

## Case-study objectives
- Build a simple web-based diet-planning demonstration.
- Containerize the application with Docker.
- Automate testing and image delivery using Jenkins CI/CD.
- Deploy and manage replicas using Kubernetes.
- Understand integration among GitHub, Docker Hub, Jenkins and Kubernetes.
