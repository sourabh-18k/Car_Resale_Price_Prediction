pipeline {
    agent any

    environment {
        IMAGE_NAME = "car-price-app"
        TAG = "latest"
        DOCKER_USER = "sourabh0718"
        DOCKER_REPO = "sourabh0718/car-price-app"
    }

    stages {
        stage("Install Docker CLI") {
            steps {
                echo "🛠️ Installing Docker CLI"
                sh 'apt-get update'
                sh 'apt-get install -y --no-install-recommends docker-ce-cli'
            }
        }

        stage("Clone Code") {
            steps {
                echo "🔄 Cloning the code"
                git url: "https://github.com/sourabh-18k/Car_Resale_Price_Prediction.git", branch: "main"
            }
        }

        stage("Build") {
            steps {
                echo "🐳 Building the Docker image"
                sh "docker build -t ${IMAGE_NAME}:${TAG} ."
            }
        }

        stage("Push to Docker Hub") {
            steps {
                echo "📤 Pushing to Docker Hub"
                withCredentials([usernamePassword(credentialsId: "docker-hub-credentials", passwordVariable: "docker-hub-pass", usernameVariable: "docker-hub-id")]) {
                    sh """
                        echo Logging into Docker Hub
                        docker login -u ${docker-hub-id} -p ${docker-hub-pass}
                        docker tag ${IMAGE_NAME}:${TAG} ${DOCKER_REPO}:${TAG}
                        docker push ${DOCKER_REPO}:${TAG}
                    """
                }
            }
        }

        stage("Deploy") {
            steps {
                echo "🚀 Deploying the container"
                sh """
                    echo Stopping existing containers
                    docker-compose down
                    echo Deploying the new container
                    docker-compose up -d
                """
            }
        }
    }

    post {
        always {
            echo "🎬 Pipeline completed."
        }
        failure {
            echo "❌ Pipeline failed."
        }
    }
}
