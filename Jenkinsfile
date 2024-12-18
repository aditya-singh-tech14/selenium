pipeline {
    agent any

    environment {
        PYTHON_ENV = "/usr/bin/python3"  // Path to Python executable
        CHROMEDRIVER_PATH = '/usr/local/bin/chromedriver'  // Path to ChromeDriver
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from the specified GitHub repository
                git branch: 'main', url: 'https://github.com/aditya-singh-tech14/selenium.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Set up a virtual environment and install dependencies
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
                    // Execute Pytest with a maximum failure threshold of 1
                    def testResult = sh(
                        script: '''
                        . venv/bin/activate
                        pytest --maxfail=1 --disable-warnings -q
                        ''',
                        returnStatus: true
                    )

                    // Fail the build if more than 1 test fails
                    if (testResult != 0) {
                        error("Test cases failed! Exceeded maximum allowed failures (maxfail=1).")
                    }
                }
            }
        }

        stage('Deploy to Production') {
            when {
                expression {
                    // Only run this stage if the tests passed successfully
                    currentBuild.result == null || currentBuild.result == 'SUCCESS'
                }
            }
            steps {
                // Add your deployment steps here
                echo 'Deploying to production...'
                sh './deploy_to_prod.sh'  // Replace with your deployment script
            }
        }
    }

    post {
        always {
            // Clean up workspace after the build
            echo 'Cleaning up...'
            deleteDir()
        }
        success {
            echo 'Build succeeded! Code has been deployed to production.'
        }
        failure {
            echo 'Build failed. Please check the test case results.'
        }
    }
}
