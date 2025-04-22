pipeline {
    agent any

    environment {
        IMAGE_NAME = "car-price-app"
        TAG = "latest"
        DOCKER_USER = "sourabh0718"
        DOCKER_REPO = "${DOCKER_USER}/${IMAGE_NAME}"
    }

    stages {
        stage("Clone Repo") {
            steps {
                echo "🔄 Cloning repository..."
                git url: "https://github.com/sourabh-18k/Car_Resale_Price_Prediction.git", branch: "main"
            }
        }

        stage("Run Tests") {
            steps {
                echo "🧪 Running basic tests using pytest..."
                sh 'pip install -r requirements.txt'
                sh 'pip install pytest'
                sh 'pytest tests/'
            }
        }

        stage("Build Docker Image") {
            steps {
                echo "🐳 Building Docker image..."
                sh "docker build -t ${IMAGE_NAME}:${TAG} ."
            }
        }

        stage("Push to Docker Hub") {
            steps {
                echo "📤 Pushing Docker image to Docker Hub..."
                withCredentials([usernamePassword(credentialsId: "docker-hub-credentials", passwordVariable: 'DOCKER_PASS', usernameVariable: 'DOCKER_USER')]) {
                    sh """
                        echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                        docker tag ${IMAGE_NAME}:${TAG} ${DOCKER_REPO}:${TAG}
                        docker push ${DOCKER_REPO}:${TAG}
                    """
                }
            }
        }

        stage("Run Container (Local)") {
            steps {
                echo "🚀 Running Docker container locally on port 8501..."
                sh "docker run -d -p 8501:8501 ${DOCKER_REPO}:${TAG}"
            }
        }
    }

    post {
        always {
            echo "✅ Pipeline complete."
        }
        failure {
            echo "❌ Pipeline failed. Check the logs."
        }
    }
}

