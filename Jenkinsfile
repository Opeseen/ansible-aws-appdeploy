pipeline{
  agent any
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
            dbendpoint: "flaskappdb.cfzrgfw3zego.us-east-1.rds.amazonaws.com"
          ]
        ])
      } 

    }
  }
}





  // ansiblePlaybook('ansible-stack/app.yml') {
  //         inventoryPath('ansible-stack/jenkins_ansible_inventory')
  //         colorizedOutput(true)
  //         credentialsId('appLogin')
  //         hostKeyChecking(false)
  //         become(true)
  //         becomeUser("root")
  //         sudo(true)
  //       }