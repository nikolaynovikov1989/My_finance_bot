pipeline {
    agent any
    stages {
        stage('restart') {
            steps {
                ansiblePlaybook credentialsId: 'gitcred', vaultCredentialsId: 'vault1', disableHostKeyChecking: true, inventory: 'hosts', extraVars: '${role}', playbook: 'playbook_restart.yml'
            }
        }
    }
}