pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t car-price-app .'
                }
            }
        }

        stage('Run Container') {
            steps {
                script {
                    // Remove existing container if already running
                    sh '''
                        docker rm -f car-price-container || true
                        docker run -d -p 8501:8501 --name car-price-container car-price-app
                    '''
                }
            }
        }
    }
}

