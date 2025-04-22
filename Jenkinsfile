pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    def image = docker.build("car-price-app")
                }
            }
        }

        stage('Run Container') {
            steps {
                script {
                    sh "docker run -d -p 8501:8501 car-price-app"
                }
            }
        }
    }
}

