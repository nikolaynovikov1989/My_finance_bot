pipeline {
    agent any
    stages {
        stage('update_bot') {
            steps {
                ansiblePlaybook credentialsId: 'gitcred', vaultCredentialsId: 'vault1', disableHostKeyChecking: true, inventory: 'hosts', playbook: 'playbook.yml'
            }
        }
    }
}