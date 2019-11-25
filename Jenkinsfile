pipeline {
  
  agent any
  
  stages {
    stage ('run docker') {
      steps {
        sh 'docker run --name jenka --network="host" maslovu/api-tests'
        sh "docker exec jenka 'pytest -s -v ApiTestsForMyrestAplic'"
      }
    }

  }
}
