pipeline {
  
  agent any
  
  stages {
    stage ('run docker') {
      steps {
        sh 'docker run --network="host" maslov/api-tests'
      }
    }
    stage('run docker') {
      steps {
        sh "docker exec -it maslovu/api-tests 'pytest -s -v ApiTestsForMyrestAplic'"
      }
    }

  }
}
