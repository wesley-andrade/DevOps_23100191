pipeline {
    agent any

    environment {
        REPO_URL = 'https://github.com/wesley-andrade/Trabalho_DevOps_23100191.git'
        BRANCH_NAME = 'main'
        DOCKER_COMPOSE = 'docker-compose'
        DOCKER_IMAGE_TAG = 'latest'
    }

    stages {
        stage('Baixar código do Git') {
            steps {
                git branch: "${BRANCH_NAME}", url: "${REPO_URL}"
            }
        }

        stage('Rodar Testes') {
            steps {
                script {
                    try {
                        sh "${DOCKER_COMPOSE} up -d mariadb flask_app"
                        sh """
                        for i in {1..10}; do
                            if curl -s http://localhost:5000/health > /dev/null; then
                                echo "Flask está pronto."
                                break
                            fi
                            echo "Aguardando o Flask iniciar..."
                            sleep 5
                        done
                        """
                        sh "${DOCKER_COMPOSE} exec flask_app python -m unittest discover -s /app/tests -p 'test_*.py' -v"
                    } catch (Exception e) {
                        currentBuild.result = 'FAILURE'
                        error "Os testes falharam: ${e.message}"
                    }
                }
            }
        }

        stage('Build e Deploy') {
            steps {
                script {
                    try {
                        sh "${DOCKER_COMPOSE} build --no-cache"
                        sh "${DOCKER_COMPOSE} up -d mariadb flask_app prometheus grafana"
                        sh 'curl -s http://localhost:9090/metrics || exit 1'
                    } catch (Exception e) {
                        error "Erro durante o build ou deploy: ${e.message}"
                    }
                }
            }
        }
    }

    post {
        always {
            echo "Pipeline finalizada."
            sh "${DOCKER_COMPOSE} down -v"
        }
        success {
            echo "Pipeline executada com sucesso!"
        }
        failure {
            echo "Pipeline falhou."
        }
    }
}
