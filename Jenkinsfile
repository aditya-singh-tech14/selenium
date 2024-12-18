pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Fetch the repository
                git url: 'https://github.com/aditya-singh-tech14/selenium.git', branch: 'driver', credentialsId: 'aditya-github-pass'

            }
        }

        stage('Install Dependencies') {
            steps {
                // Setup Python environment and install required packages
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --force-reinstall -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                // Run Selenium Pytest test cases with max failure = 1
                sh '''
                    . venv/bin/activate
                    pytest --maxfail=1 --disable-warnings -q
                '''
            }
        }

        stage('Deploy to Production') {
            when {
                // Deploy only if all test cases pass
                expression { currentBuild.result == null || currentBuild.result == 'SUCCESS' }
            }
            steps {
                // Add the provided deployment script
                writeFile file: 'deploy_to_prod.sh', text: '''#!/bin/sh

# Install dependencies, forcing reinstallation if necessary
npm install --force

# Load nvm and set the desired Node.js version
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \\. "$NVM_DIR/nvm.sh"
nvm use 20.9.0

# Verify the Node.js version
node --version

# Restart the PM2-managed process with the correct interpreter
pm2 restart 0 --update-env --interpreter "$(which node)"

# Save the current PM2 configuration
pm2 save

# Display the status of all PM2-managed processes
pm2 status
                '''
                sh '''
                    chmod +x deploy_to_prod.sh
                    ./deploy_to_prod.sh
                '''
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            deleteDir() // Clean up the workspace
        }
        failure {
            echo 'Build failed. Please check the test case results.'
        }
    }
}
