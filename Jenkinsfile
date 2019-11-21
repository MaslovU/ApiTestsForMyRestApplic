pipeline {
  agent {
    docker {
      image 'maslovu/api-tests'
      args '-it --network="host"'
    }

  }
  stages {
    stage('ApiTestsForMyrestAplic') {
      steps {
        sh 'pytest -s -v ApiTestsForMyrestAplic'
      }
    }

  }
}
