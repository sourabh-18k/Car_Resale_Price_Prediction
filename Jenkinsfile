pipeline {
    agent {
        docker {
            image 'python:3.8-slim' // Use a Python Docker image
            args '-v /tmp:/tmp' // Mount temp directory for Docker if needed
        }
    }

    environment {
        IMAGE_NAME = "car-price-app"
        TAG = "latest"
        DOCKER_USER = "sourabh0718"
        DOCKER_REPO = "sourabh0718/car-price-app"
    }

    stages {
        stage("Clone Repo") {
            steps {
                echo "🔄 Cloning repository..."
                git url: "https://github.com/sourabh-18k/Car_Resale_Price_Prediction.git", branch: "main"
            }
        }

        stage("Install Dependencies") {
            steps {
                echo "📦 Installing Python dependencies..."
                sh "pip install -r requirements.txt"
            }
        }

        stage("Run Tests") {
            steps {
                echo "🧪 Running basic tests using pytest..."
                sh "pytest tests/test_dummy.py"
            }
        }

        stage("Build Docker Image") {
            steps {
                echo "🐳 Building Docker image..."
                sh """
                docker build -t ${DOCKER_REPO}:${TAG} .
                """
            }
        }

        stage("Push to Docker Hub") {
            steps {
                echo "📤 Pushing Docker image to Docker Hub..."
                withCredentials([usernamePassword(credentialsId: "docker-hub-credentials", passwordVariable: "docker-hub-pass", usernameVariable: "docker-hub-id")]) {
                    sh """
                    echo Logging into Docker Hub
                    docker login -u ${docker-hub-id} -p ${docker-hub-pass}
                    docker tag ${DOCKER_REPO}:${TAG} ${DOCKER_USER}/${DOCKER_REPO}:${TAG}
                    docker push ${DOCKER_USER}/${DOCKER_REPO}:${TAG}
                    """
                }
            }
        }

        stage("Deploy Docker Container") {
            steps {
                echo "🚀 Deploying Docker container..."
                sh """
                docker-compose down
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
