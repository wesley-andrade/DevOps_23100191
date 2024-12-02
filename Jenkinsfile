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
                    // Subir os containers do Docker com Docker Compose
                    sh '''
                        docker-compose up --build -d
                    '''
                }
            }
        }

        stage('Verificar MariaDB') {
            steps {
                script {
                    // Esperar MariaDB ficar disponível
                    sh '''
                        for i in {1..20}; do
                            if docker-compose exec mariadb_container mysqladmin -u root -proot_password ping --silent; then
                                echo "MariaDB está pronto."
                                break
                            fi
                            echo "Aguardando MariaDB iniciar..."
                            sleep 5
                        done
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
