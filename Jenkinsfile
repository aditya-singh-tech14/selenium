pipeline {
    agent { label 'Selenium_Node' }
    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/aditya-singh-tech14/selenium.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'pytest --html=report.html'
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: 'report.html', fingerprint: true
        }
    }
}
