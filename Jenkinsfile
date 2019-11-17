pipeline {
  agent {
    docker {image 'maslovu/api-tests'}
  }
  stages {
    stage('Pull image') {
        steps {
            sh 'docker run -it --name apishkas --network="host" maslovu/api-tests'
        }
    }
    stage('Run Tests') {
      steps {
        sh 'pytest -s -v ApiTestsForMyrestAplic'
      }
    }
  }
}
