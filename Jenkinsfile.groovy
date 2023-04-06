pipeline {
    agent any
    stages {
        stage('copy') {
            steps {
              ansiblePlaybook playbook: 'playbook.yml', inventory: 'hosts', credentialsId: 'gitcred'
            }
        }
    }
}