pipeline {
    agent any
    
    environment {
        DOCKER_HUB_CREDS = credentials('docker-hub-credentials')
        // Replace with your Docker Hub username
        DOCKER_HUB_USERNAME = 'rajdipdevops'
        BACKEND_IMAGE = "${DOCKER_HUB_USERNAME}/quotegen-backend"
        FRONTEND_IMAGE = "${DOCKER_HUB_USERNAME}/quotegen-frontend"
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Build Backend') {
            steps {
                dir('backend') {
                    sh 'docker build -t ${BACKEND_IMAGE}:${BUILD_NUMBER} -t ${BACKEND_IMAGE}:latest .'
                }
            }
        }
        
        stage('Build Frontend') {
            steps {
                dir('frontend') {
                    sh 'docker build -t ${FRONTEND_IMAGE}:${BUILD_NUMBER} -t ${FRONTEND_IMAGE}:latest .'
                }
            }
        }
        
        stage('Test') {
            parallel {
                stage('Backend Tests') {
                    steps {
                        dir('backend') {
                            // Run unit tests
                            sh 'npm install'
                            sh 'npm run test:unit'
                            
                            // Run integration tests
                            sh 'npm run test:integration'
                            
                            // Run security audit
                            sh 'npm audit'
                            
                            // Code coverage
                            sh 'npm run test:coverage'
                        }
                    }
                    post {
                        always {
                            junit 'backend/test-results/*.xml'
                            publishHTML(target: [
                                allowMissing: false,
                                alwaysLinkToLastBuild: false,
                                keepAll: true,
                                reportDir: 'backend/coverage',
                                reportFiles: 'index.html',
                                reportName: 'Backend Coverage Report'
                            ])
                        }
                    }
                }
                stage('Frontend Tests') {
                    steps {
                        dir('frontend') {
                            // Run unit tests
                            sh 'npm install'
                            sh 'npm run test:unit'
                            
                            // Run e2e tests
                            sh 'npm run test:e2e'
                            
                            // Run security audit
                            sh 'npm audit'
                            
                            // Code coverage
                            sh 'npm run test:coverage'
                        }
                    }
                    post {
                        always {
                            junit 'frontend/test-results/*.xml'
                            publishHTML(target: [
                                allowMissing: false,
                                alwaysLinkToLastBuild: false,
                                keepAll: true,
                                reportDir: 'frontend/coverage',
                                reportFiles: 'index.html',
                                reportName: 'Frontend Coverage Report'
                            ])
                        }
                    }
                }
            }
        }
        
        stage('Push Images') {
            steps {
                sh 'echo $DOCKER_HUB_CREDS_PSW | docker login -u $DOCKER_HUB_CREDS_USR --password-stdin'
                sh 'docker push ${BACKEND_IMAGE}:${BUILD_NUMBER}'
                sh 'docker push ${BACKEND_IMAGE}:latest'
                sh 'docker push ${FRONTEND_IMAGE}:${BUILD_NUMBER}'
                sh 'docker push ${FRONTEND_IMAGE}:latest'
            }
        }
        
        stage('Deploy to Kubernetes') {
            steps {
                // Windows-compatible commands for update
                bat '''
                    powershell -Command "(Get-Content kubernetes/backend-deployment.yaml) -replace 'image: %BACKEND_IMAGE%:.*', 'image: %BACKEND_IMAGE%:%BUILD_NUMBER%' | Set-Content kubernetes/backend-deployment.yaml"
                    powershell -Command "(Get-Content kubernetes/frontend-deployment.yaml) -replace 'image: %FRONTEND_IMAGE%:.*', 'image: %FRONTEND_IMAGE%:%BUILD_NUMBER%' | Set-Content kubernetes/frontend-deployment.yaml"
                '''
                
                // Apply Kubernetes manifests
                bat 'kubectl apply -f kubernetes/'
            }
        }
    }
    
    post {
        always {
            sh 'docker logout'
            // Clean up workspace
            cleanWs()
        }
        success {
            // Notify on success
            echo 'Pipeline completed successfully!'
        }
        failure {
            // Notify on failure
            echo 'Pipeline failed!'
        }
    }
}