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

        stage('Rodar Testes') {
            steps {
                script {
                    // Rodar os testes criados para a aplicação
                    sh 'python3 -m unittest discover tests'  // Comando para rodar os testes com unittest
                }
            }
        }

        stage('Build e Deploy') {
            steps {
                script {
                    // Parar os containers se já estiverem rodando
                    sh 'docker-compose down'

                    // Construir as imagens Docker e subir os containers
                    sh 'docker-compose up --build -d'  // Subir ambiente com Docker Compose
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
