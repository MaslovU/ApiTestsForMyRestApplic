pipeline {
  
  agent any
  
  stages {
    stage ('run docker') {
      steps {
        sh 'docker run --network="host" maslovu/api-tests'
      }
    }
    stage('run test') {
      steps {
        sh "docker exec -it maslovu/api-tests 'pytest -s -v ApiTestsForMyrestAplic'"
      }
    }

  }
}
