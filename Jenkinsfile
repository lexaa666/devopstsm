pipeline {
    agent any 
    stages {
        stage('Stage 1') {
            steps {
                git branch: 'main', 
                credentialsId: 'jenkins_github_tsm', 
                url: 'https://github.com/lexaa666/devopstsm.git'
            }
        }
        stage('Stage 2') {
            steps {
                sh 'ansible -i /home/tsmadmin/lesson35/inventory.ini -m ping  all'
            }
        }
        stage('Stage 3') {
            steps {
                sh 'pwd'
                sh 'ip a'
            }
        }
        stage('Bot_python') {
            steps {
                sh 'python3 /home/tsmadmin/lesson35/telegram_send.py'
            }
        }
    }
}