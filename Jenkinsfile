pipeline {
    agent any

    stages {

        stage('Clone') {
            steps {
                git branch: 'main', url: 'https://github.com/shalma4/azure-aks-jenkins-demo.git'
            }
        }

        stage('Build Docker') {
            steps {
                sh 'docker build -t shalmaacr.azurecr.io/flask-app:v1 .'
            }
        }

        stage('Push Image') {
            steps {
                sh 'docker push shalmaacr.azurecr.io/flask-app:v1'
            }
        }

        stage('Deploy') {
            steps {
                sh 'kubectl apply -f deployment.yaml'
                sh 'kubectl apply -f service.yaml'
            }
        }
    }
}
