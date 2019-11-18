pipeline {
  agent {
    docker {
      image 'maslovu/api-tests'
      args '-it --network="host"'
    }

  }
  stages {
    stage('Tests') {
      steps {
        sh 'pytest -s -v ApiTestsForMyrestAplic'
      }
    }

  }
}
