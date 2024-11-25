pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                    sh 'docker compose down -v'
                    sh 'docker compose build'
                }
            }
        }

        stage('Start') {
            steps {
                script {
                    sh 'docker compose up -d'
                }
            }
        }
    }

}