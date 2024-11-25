pipeline {
    agent any

    environment {
        DOCKER_IMAGE_NAME = 'trabalhodevops_flask_app'
        DOCKER_REGISTRY = 'docker.io'
        DOCKER_TAG = 'latest'
    }

    stages {
        stage('Baixar Código do Git') {
            steps {
                script {
                    // Clonar o repositório do Git
                    git branch: 'main', url: 'https://github.com/wesley-andrade/DevOps_23100191.git'
                }
            }
        }

        stage('Build e Deploy') {
            steps {
                script {
                    // Construir a imagem Docker para a aplicação
                    sh "docker build -t ${DOCKER_REGISTRY}/${DOCKER_IMAGE_NAME}:${DOCKER_TAG} ."

                    // Subir o ambiente Docker
                    sh "docker-compose up --build -d"
                    
                    // Verificar os containers em execução
                    sh 'docker ps'
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline finalizada com sucesso!'
        }

        failure {
            echo 'Houve um erro na pipeline.'
        }
    }
}
