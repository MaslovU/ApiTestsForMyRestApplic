pipeline {
  agent {
    docker {
      image 'maslovu/api-tests'
      args "--network='host'"
    }

  }
  stages {
    stage('ApiTestsForMyrestAplic') {
      steps {
        sh 'pytest -s -v Test'
      }
    }

  }
}
