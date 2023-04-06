pipeline {
    agent any
    stages {
        stage('restart') {
            steps {
                ansiblePlaybook credentialsId: 'gitcred', vaultCredentialsId: 'vault1', disableHostKeyChecking: true, inventory: 'hosts', extras: '${role}', playbook: 'playbook_restart.yml'
            }
        }
    }
}