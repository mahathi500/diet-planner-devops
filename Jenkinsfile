pipeline {
    agent any
    environment {
        IMAGE_NAME = "mahathinalagandla/diet-planner""
        IMAGE_TAG = "latest"
    }
    stages {
        stage('Install Dependencies') {
            steps { bat 'python -m pip install -r requirements.txt' }
        }
        stage('Run Tests') {
            steps { bat 'python -m pytest -v' }
        }
        stage('Build Docker Image') {
            steps { bat 'docker build -t %IMAGE_NAME%:%IMAGE_TAG% .' }
        }
        stage('Login to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_TOKEN')]) {
                    bat 'echo %DOCKER_TOKEN%| docker login -u %DOCKER_USER% --password-stdin'
                }
            }
        }
        stage('Push Docker Image') {
            steps { bat 'docker push %IMAGE_NAME%:%IMAGE_TAG%' }
        }
        stage('Deploy to Kubernetes') {
            steps {
                bat 'kubectl apply -f deployment.yaml'
                bat 'kubectl apply -f service.yaml'
                bat 'kubectl rollout status deployment/diet-planner --timeout=120s'
            }
        }
    }
    post {
        success { echo 'Diet Planner pipeline completed successfully!' }
        failure { echo 'Pipeline failed. Check the console output.' }
        always { bat 'docker logout' }
    }
}
