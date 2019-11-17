pipeline {
  agent {
    docker {
      image 'maslovu/api-tests'
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