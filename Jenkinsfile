pipeline {
  
  agent any
  
  stages {
    stage ('run docker') {
      steps {
        sh "docker run -i --name apishkas --network='host' maslovu/api-tests"
        sh "docker exec apishkas 'pytest -s -v ApiTestsForMyrestAplic'"
      }
    }
  }
}
