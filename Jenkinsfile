pipeline{
  
  agent any

  environment {
    dbEndpoint = credentials('dbEndpoint')
  }

  stages{
    stage('CICD with ansible-jenkins'){
      steps {
        ansiblePlaybook([
          inventory: "ansible-stack/jenkins_ansible_inventory",
          playbook: "ansible-stack/app.yml",
          installation: "ansible",
          colorized: true,
          credentialsId: "appLogin",
          disableHostKeyChecking: true,
          become: true,
          becomeUser: "root",
          extraVars: [
            dbendpoint: "${dbEndpoint}"
          ]
        ])
      } 

    }
  }
}