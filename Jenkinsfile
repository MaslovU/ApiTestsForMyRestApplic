pipeline {
  agent {
    docker {
      args '''--network=\'host\'
--name apishkas'''
      image 'maslovu/api-tests'
    }

  }
  stages {
    stage('Pytest') {
      steps {
        sh 'pytest -s -v ApiTestsForMyrestAplic'
      }
    }

  }
}