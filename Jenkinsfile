pipeline {
    agent any

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
                bat 'python -m pytest'
            }
        }
    }
}