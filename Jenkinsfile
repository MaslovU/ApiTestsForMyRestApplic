pipeline {
  agent {
    docker {
      image 'maslovu/api-tests'
      args '--network=\'host\''
    }

  }
  stages {
    stage('') {
      steps {
        sh 'pytest -s -v ApiTestsForMyrestAplic'
      }
    }

  }
}