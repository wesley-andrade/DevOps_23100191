pipeline {
    agent any

    environment {
        REPO_URL = 'https://github.com/wesley-andrade/Trabalho_DevOps_23100191.git'  // URL do repositório
        BRANCH_NAME = 'main'                                                      // Nome do branch
        DOCKER_COMPOSE = 'docker-compose'                                         // Comando para Docker Compose
    }

    stages {
        stage('Baixar código do Git') {
            steps {
                git branch: "${BRANCH_NAME}", url: "${REPO_URL}"
            }
        }

        stage('Verificar Python e pip') {
            steps {
                sh 'python3 --version'
                sh 'pip --version'
            }
        }

        stage('Instalar Dependências') {
            steps {
                script {
                    // Instalar as dependências diretamente no ambiente Jenkins
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Rodar Testes') {
            steps {
                script {
                    // Rodar os testes dentro do container
                    sh '${DOCKER_COMPOSE} exec flask_app python -m unittest discover /app/tests'
                }
            }
        }

        stage('Build e Deploy') {
            steps {
                script {
                    // Parar e remover os containers existentes
                    sh '${DOCKER_COMPOSE} down --volumes --remove-orphans'

                    // Construir as imagens Docker e subir os containers
                    sh '${DOCKER_COMPOSE} up --build -d'
                }
            }
        }

        stage('Verificar Monitoramento') {
            steps {
                script {
                    // Verificar se o serviço está rodando no Prometheus
                    sh """
                    for i in {1..10}; do
                        if curl -s http://localhost:9090/ > /dev/null; then
                            echo "Monitoramento do Prometheus funcionando."
                            break
                        fi
                        echo "Aguardando Prometheus iniciar..."
                        sleep 5
                    done
                    """
                }
            }
        }
    }

    post {
        always {
            echo "Pipeline finalizada."
        }
        success {
            echo "Pipeline executada com sucesso!"
        }
        failure {
            echo "Pipeline falhou. Verifique os logs."
        }
    }
}
