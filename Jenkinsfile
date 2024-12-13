pipeline {
    agent { label 'Selenium-Node' }
    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/aditya-singh-tech14/selenium.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh '''
                python3 -m venv venv
                source venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }
        stage('Run Tests') {
            steps {
                sh 'pytest --html=report.html'
            }
        }
    }
}
