pipeline {
    agent any

    environment {
        IMAGE_NAME = 'my-static-website'
        CONTAINER_NAME = 'static-site-container'
        HOST_PORT = '8080'
        CONTAINER_PORT = '80'
    }

    stages {
        stage('Clone Repository') {
            steps {
                echo "🔄 Cloning website code..."
                git 'git@github.com:sourabh-18k/website.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "🐳 Building Docker image..."
                sh "docker build -t ${IMAGE_NAME} ."
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    echo "🏃 Running Docker container..."
                    // Stop and remove previous container if it exists
                    sh "docker stop ${CONTAINER_NAME} || true"
                    sh "docker rm ${CONTAINER_NAME} || true"

                    // Run the new container
                    sh "docker run -d --name ${CONTAINER_NAME} -p ${HOST_PORT}:${CONTAINER_PORT} ${IMAGE_NAME}"
                    echo "✅ Static website running at http://localhost:${HOST_PORT}"
                }
            }
        }
    }

    post {
        success {
            echo "🎉 Pipeline finished successfully! Static website is live at http://localhost:${env.HOST_PORT}"
        }
        failure {
            echo "💔 Pipeline failed! Check the console output for errors."
        }
    }
}
