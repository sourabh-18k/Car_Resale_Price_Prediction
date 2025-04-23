pipeline {
    agent any

    environment {
        IMAGE_NAME = "car-price-app"
        TAG = "latest"
        DOCKER_USER = "sourabh0718"
        DOCKER_REPO = "sourabh0718/car-price-app"
        HOST_PORT = '8083' // host
        CONTAINER_PORT = '5000' 
    }

    stages {
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

        stage("Run Container") {
            steps {
                script {
                    echo "🚀 Running the Docker container"
                    // Stop and remove previous container if it exists
                    sh "docker stop ${IMAGE_NAME}-${TAG} || true"
                    sh "docker rm ${IMAGE_NAME}-${TAG} || true"

                    // Run the new container
                    sh "docker run -d --name ${IMAGE_NAME}-${TAG} -p ${HOST_PORT}:${CONTAINER_PORT} ${IMAGE_NAME}:${TAG}"
                    echo "✅ Application running at http://localhost:${HOST_PORT}"
                }
            }
        }

        stage("Push to Docker Hub") {
            steps {
                echo "📤 Pushing to Docker Hub"
                withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh """
                        echo "\$DOCKER_PASS" | docker login -u "\$DOCKER_USER" --password-stdin
                        docker tag ${IMAGE_NAME}:${TAG} \$DOCKER_USER/${IMAGE_NAME}:${TAG}
                        docker push \$DOCKER_USER/${IMAGE_NAME}:${TAG}
                    """
                }

            }
        }

        
    }

    post {
        success {
            echo "🎉 Pipeline finished successfully! Application is live at http://localhost:${env.HOST_PORT}"
        }
        failure {
            echo "💔 Pipeline failed!"
        }
    }
}
