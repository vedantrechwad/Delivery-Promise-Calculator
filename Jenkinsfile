pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build and Test') {
            steps {
                bat '"C:\\DevTools\\apache-maven-3.9.16\\bin\\mvn.cmd" clean test package'
            }
        }

        stage('Docker Check') {
            steps {
                bat '''
                docker --version
                docker ps
                '''
            }
        }

        stage('Docker Build') {
            steps {
                bat 'docker build -t delivery-promise-calculator:1.0 .'
            }
        }

        stage('Docker Deploy') {
            steps {
                bat '''
                docker rm -f delivery-promise-app 2>nul || exit /b 0
                docker run -d --name delivery-promise-app -p 8766:8765 delivery-promise-calculator:1.0
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                bat '''
                docker ps --filter "name=delivery-promise-app"
                echo Docker deployment completed successfully.
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully. Docker application deployed on port 8766.'
        }

        failure {
            echo 'Pipeline failed. Check the stage logs.'
        }
    }
}
