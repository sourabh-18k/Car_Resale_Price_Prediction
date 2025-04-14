pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE = 'car-price-prediction-image'
    }

    stages {
        stage('Checkout') {
            steps {
                // Pull the latest code from the repository
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install the dependencies using the requirements.txt file
                script {
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image for the project
                    sh 'docker build -t $DOCKER_IMAGE .'
                }
            }
        }

        stage('Run Tests') {
            steps {
                // Example of running tests (if you add them later)
                script {
                    // Running pytest to check if everything is working
                    sh 'pytest tests/'
                }
            }
        }

        stage('Run Model Training') {
            steps {
                script {
                    // Run the model training inside the Docker container
                    sh 'docker run --rm $DOCKER_IMAGE'
                }
            }
        }

        stage('Deploy') {
            steps {
                // You can add deployment steps here if applicable
                echo 'Deploying model...'
            }
        }
    }

    post {
        always {
            // Clean up, e.g., remove Docker images if you need to
            sh 'docker system prune -f'
        }
    }
}
