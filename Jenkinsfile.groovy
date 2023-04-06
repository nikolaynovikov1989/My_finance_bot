pipeline {
    agent any
    stages {
        stage('copy') {
            steps {
                ansiblePlaybook credentialsId: 'gitcred', vaultCredentialsId: 'vault1', disableHostKeyChecking: true, inventory: 'hosts', playbook: 'playbook.yml'
            }
        }
    }
}