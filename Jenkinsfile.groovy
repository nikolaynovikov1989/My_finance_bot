pipeline {
    agent any
    stages {
        stage('copy') {
            steps {
                ansiblePlaybook credentialsId: 'gitcred', disableHostKeyChecking: true, inventory: 'hosts', playbook: 'playbook.yml'
            }
        }
    }
}