pipeline {
    agent any

    environment {
        PYTHON_ENV = "/usr/bin/python3"  // Path to Python executable (adjust if needed)
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout your code from the GitHub repository
                git branch: 'main', url: 'https://github.com/aditya-singh-tech14/selenium.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Install required Python packages
                    sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Run the Pytest test cases
                    sh '''
                    . venv/bin/activate
                    pytest --maxfail=1 --disable-warnings -q
                    '''
                }
            }
        }
    }

    post {
        always {
            // Clean up actions if needed
            echo 'Cleaning up...'
            deleteDir()  // Clean workspace after build
        }
        success {
            echo 'Tests passed!'
        }
        failure {
            echo 'Tests failed!'
        }
    }
}
