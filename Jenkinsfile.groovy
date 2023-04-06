pipeline {
    agent any
    stages {
        stage('copy') {
            steps {
                ansiblePlaybook credentialsId: 'gitcred', vaultCredentialsId: '/home/ansible_user/ansible-playbook/vault.txt', disableHostKeyChecking: true, inventory: 'hosts', playbook: 'playbook.yml'
            }
        }
    }
}