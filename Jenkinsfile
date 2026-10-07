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
                    if exist "%DEPLOY_DIR%\\application.log" del /Q "%DEPLOY_DIR%\\application.log"
                    set "JENKINS_SERVER_COOKIE=dontKillMe"
                    set "JENKINS_NODE_COOKIE=dontKillMe"
                    start "Delivery Promise Calculator" /B cmd /c "java -jar \"%DEPLOY_DIR%\\%JAR_NAME%\" > \"%DEPLOY_DIR%\\application.log\" 2>&1"
                    timeout /t 5 /nobreak >nul
                    echo Application launch command completed.
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully. Application deployment command completed.'
        }
        failure {
            echo 'Pipeline failed. Check the stage logs for details.'
        }
    }
}
