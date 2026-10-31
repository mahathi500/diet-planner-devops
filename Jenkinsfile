pipeline {
    agent any
    environment {
        IMAGE_NAME = "mahathinalagandla/diet-planner"
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
        stage('Docker Login') {
            steps {
                bat 'docker login -u mahathinalagandla -p Mahathi@123'
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
