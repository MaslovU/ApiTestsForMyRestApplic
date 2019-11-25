pipeline {
  
  agent any
  
  stages {
    
    stage('run docker') {
      steps {
        sh "docker run --network='host' maslovu/api-tests"
      }
    }

  }
}
