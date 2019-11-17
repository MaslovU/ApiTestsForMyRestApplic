pipeline {
  agent {
    docker {
      image 'maslovu/api-tests'
    }

  }
  stages {
    stage('Tests') {
      steps {
        sh 'sudo pytest -s -v ApiTestsForMyrestAplic'
      }
    }

  }
}
