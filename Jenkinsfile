pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    credentialsId: 'swimmingid', // The ID you set earlier
                    url: 'https://github.com/Svhp7592/Swimmingpoolproject.git'
            }
        }
        stage('Build') {
            steps {
                echo 'Building project...'
                // Add build steps here
            }
        }
        stage('Run Tests') {
            steps {
                echo 'Running tests...'
                // Add test execution commands here
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                // Add deployment steps here
            }
        }
    }
}