stage('Checkout'){
 git clone repo
}

stage('Build'){
 docker build -t shalma/log-analyzer:v1 .
}

stage('Push'){
 docker push shalma/log-analyzer:v1
}
