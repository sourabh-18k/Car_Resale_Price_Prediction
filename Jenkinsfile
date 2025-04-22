pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'car-price-app'
        DOCKER_TAG = "${BUILD_NUMBER}"
        DOCKER_USER = "sourabh0718"
        DOCKER_REPO = "sourabh0718/car-price-app"
        PYTHON_PATH = '/usr/local/bin/python3'
        DOCKER_PATH = '/usr/local/bin/docker'
        DOCKER_HOST = 'unix:///var/run/docker.sock'
        DOCKER_CONFIG = ''
    }

    stages {
        stage('Install Python & pip') {
            steps {
                script {
                    echo "🔧 Installing Python & pip..."
                    sh """
                        apt-get update
                        apt-get install -y python3 python3-pip
                    """
                }
            }
        }

        stage('Clone Repo') {
            steps {
                echo "🔄 Cloning repository..."
                git url: "https://github.com/sourabh-18k/Car_Resale_Price_Prediction.git", branch: "main"
            }
        }

        stage('Install Dependencies') {
            steps {
                echo "📦 Installing Python dependencies..."
                sh "pip install -r requirements.txt"
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "🐳 Building Docker image..."
                sh '''
                    # Setup Docker config without credsStore
                    mkdir -p ~/.docker
                    echo '{ "credsStore": "" }' > ~/.docker/config.json

                    # Check Docker installation
                    if [ ! -x "${DOCKER_PATH}" ]; then
                        echo "Docker is not installed or not executable at ${DOCKER_PATH}"
                        exit 1
                    fi
                    
                    # Check Docker daemon
                    if ! ${DOCKER_PATH} info &> /dev/null; then
                        echo "Docker daemon is not running or not accessible"
                        exit 1
                    fi
                    
                    # Check Dockerfile existence
                    if [ ! -f "Dockerfile" ]; then
                        echo "Dockerfile not found in the workspace"
                        exit 1
                    fi
                    
                    echo "Building Docker image..."
                    DOCKER_HOST=${DOCKER_HOST} DOCKER_CONFIG=${DOCKER_CONFIG} ${DOCKER_PATH} build --progress=plain -t ${DOCKER_REPO}:${DOCKER_TAG} .
                '''
            }
        }

        stage('Deploy') {
            when {
                branch 'main'
            }
            steps {
                script {
                    echo "🚀 Deploying Docker container..."
                    sh """
                        docker-compose down
                        docker-compose up -d
                    """
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
