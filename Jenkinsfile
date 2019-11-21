pipeline {
  agent { sh 'docker run -it --name apishkas --network='host' maslov/api-tests'}
  
  stages {
    
    stage('run tests') {
      steps {
        sh 'pytest -s -v ApiTestsForMyrestAplic'
      }
    }

  }
}
