pipeline {
  
  agent any
  
  stages {
    
    stage('run docker') {
      steps {
        sh "docker run -it --network='host' maslov/api-tests"
      }
    }
     stage('run test') {
      steps {
        sh 'pytest -s -v ApiTestsForMyrestAplic'
      }
    }
  }
}
