pipeline {
  
  agent any
  
  stages {
    stage ('run docker') {
      steps {
        sh "docker run -i --name apishkas --network='host' maslov/api-tests"
      }
    }
    
    stage ('run tests') {
      steps {

        sh "docker exec jenka 'pytest -s -v ApiTestsForMyrestAplic'"
      }
    }

  }
}
