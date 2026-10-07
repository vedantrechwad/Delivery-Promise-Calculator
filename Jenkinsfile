pipeline {
    agent any

    environment {
        MAVEN = 'C:\\DevTools\\apache-maven-3.9.16\\bin\\mvn.cmd'
        DEPLOY_DIR = 'C:\\DeliveryPromise'
        JAR_NAME = 'delivery-promise-calculator-0.0.1-SNAPSHOT.jar'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build and Test') {
            steps {
                bat '''
                    call "%MAVEN%" clean test package
                '''
            }
        }

        stage('Archive Artifact') {
            steps {
                archiveArtifacts artifacts: 'target/*.jar', fingerprint: true
            }
        }

        stage('Deploy') {
            steps {
                bat '''
                    if not exist "%DEPLOY_DIR%" mkdir "%DEPLOY_DIR%"
                    copy /Y "target\\%JAR_NAME%" "%DEPLOY_DIR%\\%JAR_NAME%"
                '''
            }
        }

        stage('Start Application') {
            steps {
                bat '''
                    echo Starting Delivery Promise Calculator...
                    set "JENKINS_SERVER_COOKIE=dontKillMe"
                    set "JENKINS_NODE_COOKIE=dontKillMe"
                    start "" /B java -jar "%DEPLOY_DIR%\\%JAR_NAME%"
                    powershell -NoProfile -Command "Start-Sleep -Seconds 5"
                    echo Application launch command completed.
                    echo Application should be available at http://localhost:8765
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully. Application deployed on port 8765.'
        }
        failure {
            echo 'Pipeline failed. Check the stage logs for details.'
        }
    }
}
