pipeline {
  agent {docker}
  stages {
    stage('Clone repo') {
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
