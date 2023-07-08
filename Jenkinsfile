pipeline{
  agent any
  stages{
    stage('CICD with ansible-jenkins'){
      steps {
        ansiblePlaybook('ansible-stack/app.yml') {
          inventoryPath('ansible-stack/jenkins_ansible_inventory')
          colorized: true
          credentialsId('appLogin')
          hostKeyChecking(false)
          become(true)
          becomeUser("root")
          sudo(true)
        }
      } 

    }
  }
}