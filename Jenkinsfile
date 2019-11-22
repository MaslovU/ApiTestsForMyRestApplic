pipeline {
  agent {
    docker {
      image 'maslovu/api-tests'
    }

  }
  stages {
    stage('run docker') {
      steps {
        sh 'sh "docker run -it --name apishkas --network=\'host\' maslov/api-tests"'
      }
    }

    stage('run tests') {
      steps {
        sh 'sh \'pytest -s -v ApiTestsForMyrestAplic\''
      }
    }

  }
}