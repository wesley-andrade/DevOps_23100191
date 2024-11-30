pipeline {
    agent any

    environment {
        REPO_URL = 'https://github.com/wesley-andrade/Trabalho_DevOps_23100191.git'  // URL do repositório
        BRANCH_NAME = 'main'                                                      // Nome do branch
    }

    stages {
        stage('Baixar código do Git') {
            steps {
                // Clonar o repositório do Git
                git branch: "${BRANCH_NAME}", url: "${REPO_URL}"
            }
        }

        stage('Build e Deploy') {
            steps {
                script {
                    // Construir as imagens Docker para cada serviço
                    sh '''
                        docker-compose build
                    '''

                    // Subir os containers do Docker com Docker Compose
                    sh '''
                        docker-compose up -d
                    '''
                }
            }
        }

        stage('Rodar Testes') {
            steps {
                script {
                    // Aguardar o serviço ser iniciado
                    sh 'sleep 40' 

                    // Rodar os testes dentro do container Flask
                    sh '''
                        docker-compose exec flask_app python3 -m unittest discover /app/tests
                    '''
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline executada com sucesso!'
        }
        failure {
            echo 'A pipeline falhou.'
        }
    }
}
