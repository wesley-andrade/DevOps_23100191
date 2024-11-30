pipeline {
    agent any

    environment {
        REPO_URL = 'https://github.com/wesley-andrade/Trabalho_DevOps_23100191.git'
        BRANCH_NAME = 'main'
        DOCKER_COMPOSE = 'docker-compose'
    }

    stages {
        stage('Preparar Ambiente e Clonar Repositório') {
            steps {
                script {
                    // Clonar o repositório
                    git branch: "${BRANCH_NAME}", url: "${REPO_URL}"
                    
                    // Remover containers antigos e garantir que não há volumes antigos
                    sh "${DOCKER_COMPOSE} down -v"
                    sh "${DOCKER_COMPOSE} build --no-cache"
                }
            }
        }

        stage('Subir Contêineres e Executar Testes') {
            steps {
                script {
                    // Subindo os containers necessários para o teste
                    sh "${DOCKER_COMPOSE} up -d mariadb flask prometheus grafana"

                    // Esperar os containers subirem e estarem prontos
                    sh 'sleep 45'  // Espera mais tempo para garantir que o banco de dados e o Flask estejam prontos

                    // Rodar os testes no container Flask
                    try {
                        sh "${DOCKER_COMPOSE} exec flask_app python -m unittest /app/tests/test_app.py"
                    } catch (Exception e) {
                        currentBuild.result = 'FAILURE'
                        error "Os testes falharam! A pipeline foi interrompida."
                    }
                }
            }
        }

        stage('Verificar Status e Manter Ambiente') {
            steps {
                script {
                    // Verificar se os serviços estão de fato funcionando, como o Flask e o Prometheus
                    sh 'curl -s http://localhost:9090/metrics'  // Verificar se o Prometheus está coletando métricas

                    // Manter a aplicação rodando em segundo plano
                    sh "${DOCKER_COMPOSE} up -d mariadb flask prometheus grafana"
                }
            }
        }
    }

    post {
        always {
            // Realizar limpeza após a execução
            echo "Pipeline finalizada."
        }
        success {
            // Caso tudo tenha ocorrido bem
            echo "Pipeline executada com sucesso!"
        }
        failure {
            // Em caso de falha, parar os containers e volumes
            sh "${DOCKER_COMPOSE} down -v"
            echo "Pipeline falhou. Todos os containers foram parados e removidos."
        }
    }
}
