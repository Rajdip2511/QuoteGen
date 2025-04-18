pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                script {
                    checkout([
                        $class: 'GitSCM',
                        branches: [[name: 'origin/main']],
                        doGenerateSubmoduleConfigurations: false,
                        extensions: [],
                        userRemoteConfigs: [[url: 'https://github.com/Rajdip2511/QuoteGen.git']]
                    ])
                }
            }
        }
        stage('Build Backend Image') {
            steps {
                sh '/usr/bin/docker --version' // Just to test if it's found
                sh 'cd backend && /usr/bin/docker build -t my-quotegen-backend .'
            }
        }
        stage('Build Frontend Image') {
            steps {
                sh 'cd frontend && /usr/bin/docker build -t my-quotegen-frontend .'
            }
        }
    }
}