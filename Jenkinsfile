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

        stage('Iniciar Containers') {
            steps {
                script {
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
                    // Rodar os testes dentro do container Flask
                    sh '''
                        docker-compose exec flask_app python3 -m unittest discover /app/tests
                    '''
                }
            }
        }

        stage('Build e Deploy') {
            steps {
                script {
                    // Fazer o build e reiniciar os containers do Docker
                    sh '''
                        docker-compose up --build -d
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
