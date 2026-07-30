pipeline {

    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                url: 'https://github.com/shalma4/azure-aks-jenkins-demo.git'
            }
        }


        stage('Build') {
            steps {
                sh '''
                docker build -t shalma/log-analyzer:v1 .
                '''
            }
        }


        stage('Push') {
            steps {
                sh '''
                docker push shalma/log-analyzer:v1
                '''
            }
        }


        stage('Deploy to AKS') {
            steps {
                sh '''
                kubectl apply -f deployment.yaml
                kubectl apply -f service.yaml
                '''
            }
        }

    }
}
