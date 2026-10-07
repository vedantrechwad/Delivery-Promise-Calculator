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
                powershell '''
                    $jar = Join-Path $env:DEPLOY_DIR $env:JAR_NAME

                    $existing = Get-CimInstance Win32_Process |
                        Where-Object {
                            $_.Name -eq 'java.exe' -and
                            $_.CommandLine -like "*$env:JAR_NAME*"
                        }

                    foreach ($process in $existing) {
                        Stop-Process -Id $process.ProcessId -Force
                    }

                    Start-Process `
                        -FilePath "java.exe" `
                        -ArgumentList "-jar `"$jar`"" `
                        -WorkingDirectory $env:DEPLOY_DIR
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
