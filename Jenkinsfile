pipeline {
    agent any

    environment {
        REPO_URL = 'https://github.com/wesley-andrade/Trabalho_DevOps_23100191.git' // URL do repositório
        BRANCH_NAME = 'main'                                                      // Nome do branch
        DOCKER_COMPOSE = 'docker-compose'                                         // Comando para Docker Compose
    }

    stages {
        stage('Baixar código do Git') {
            steps {
                git branch: "${BRANCH_NAME}", url: "${REPO_URL}"
            }
        }

        stage('Subir Serviços') {
            steps {
                script {
                    sh "${DOCKER_COMPOSE} up -d"  // Subir serviços em segundo plano
                }
            }
        }

        stage('Executar Testes') {
            steps {
                script {
                    // Esperar os containers subirem
                    sh 'sleep 20'

                    // Executar os testes no container Flask
                    sh """
                    ${DOCKER_COMPOSE} exec flask_app python -m unittest /app/tests/test_app.py
                    """
                }
            }
        }
    }

    post {
        always {
            echo "Finalizando pipeline e desmontando containers."
            sh "${DOCKER_COMPOSE} down -v"  // Remover containers e volumes
        }
        success {
            echo "Pipeline executada com sucesso!"
        }
        failure {
            echo "Pipeline falhou. Verifique os logs."
        }
    }
}
