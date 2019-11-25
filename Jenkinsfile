pipeline {
  
  agent any
  
  stages {
    
    stage('run docker') {
      steps {
        sh "docker exec -it maslovu/api-tests 'pytest -s -v ApiTestsForMyrestAplic'"
      }
    }

  }
}
