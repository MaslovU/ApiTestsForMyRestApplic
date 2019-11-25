pipeline {
  
  agent any
  
  stages {
    
    stage('run docker') {
      steps {
        sh "docker exec -it --network='host' maslovu/api-tests 'pytest -s -v ApiTestsForMyrestAplic'"
      }
    }

  }
}
