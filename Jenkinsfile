pipeline {
  
  agent any
  
  stages {
    
    stage('run docker') {
      steps {
        sh 'docker run --name apishkas --network=\'host\' maslovu/api-tests'
      }
    }
    
    stage('run tests') {
      steps {
        sh 'pytest -s -v ApiTestsForMyrestAplic'
      }
    }
  }
}
