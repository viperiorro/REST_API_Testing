pipeline {
    agent any

    environment {
        EMAIL = credentials('notes_email')
        PASSWORD = credentials('notes_password')
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/viperiorro/REST_API_Testing'
            }
        }

        stage('Set Path') {
            steps {
                script {
                    env.PATH = "C:\\Users\\Oleksandr_Andriianov\\AppData\\Local\\Programs\\Python\\Python311;${env.PATH}"
                }
            }
        }

        stage('Setup Environment') {
            steps {
                bat 'python -m pip install --upgrade pip'
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                bat 'python -m pytest -ra --junit-xml=test-results.xml'
            }
        }
    }

    post {
        always {
            junit 'test-results.xml'
        }

        failure {
            echo "The pipeline has failed!"
        }
    }
}