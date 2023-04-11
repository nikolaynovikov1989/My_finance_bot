pipeline {
    agent any
    stages {
        stage('update_bot') {
            steps {
                ansiblePlaybook credentialsId: 'gitcred', vaultCredentialsId: 'vault1', disableHostKeyChecking: true, inventory: 'hosts', playbook: 'playbook.yml'
            }
        }
        stage('Start_Bot') {
            steps {
                build job: '/job/restart/configure', parameters: [[$class: 'StringParameterValue', name: 'role', value: start]]
}
    }
}