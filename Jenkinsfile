pipeline {
  agent {
    docker {
      image 'maslovu/api-test'
      args '''--network=\'host\'
--name apishkas'''
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