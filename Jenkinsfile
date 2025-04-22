pipeline {
    agent any

    
        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("car-price-app")
                }
            }
        }

        stage('Run Container') {
            steps {
                script {
                    dockerImage.run("-d -p 8501:8501")
                }
            }
        }
    }
}

