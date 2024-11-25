pipeline {
    agent any

    environment {
        // Variáveis globais, se necessário
        DOCKER_IMAGE_NAME = 'trabalhodevops_flask_app'
        DOCKER_REGISTRY = 'docker.io'
        DOCKER_TAG = 'latest'
        DOCKER_COMPOSE = '/usr/local/bin/docker-compose'
    }

    stages {
        stage('Baixar Código do Git') {
            steps {
                script {
                    // Baixar o código do repositório
                    git branch: 'main', url: 'https://github.com/wesley-andrade/DevOps_23100191.git'
                }
            }
        }

        stage('Build e Deploy') {
            steps {
                script {
                    // Construir a imagem Docker para a aplicação Flask
                    sh "docker build -t ${DOCKER_REGISTRY}/${DOCKER_IMAGE_NAME}:${DOCKER_TAG} ."

                    // Subir o ambiente Docker com Docker Compose
                    sh "${DOCKER_COMPOSE} up --build -d"
                    
                    // Verificar se o container da aplicação está funcionando
                    sh 'docker ps'
                    
                    // Aguardar a aplicação estar disponível antes de rodar o monitoramento
                    sleep(time: 30, unit: 'SECONDS')

                    // Subir o Grafana e Prometheus (caso estejam configurados)
                    // Caso queira garantir que o monitoramento esteja funcionando
                    sh 'docker-compose -f docker-compose-monitoring.yml up -d'
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
