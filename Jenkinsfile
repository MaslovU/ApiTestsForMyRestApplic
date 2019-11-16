pipeline {
  agent {
    docker {
      image 'maslovu/api-test'
      args '''--network='host''''
    }

  }
  stages {
    stage('Loading') {
      steps {
        sh 'pytest -s -v ApiTestsForMyrestAplic'
      }
    }

  }
}
