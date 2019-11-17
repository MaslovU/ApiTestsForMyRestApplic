pipeline {
  agent any

  stages {
    stage('Clone repo') {
        steps {
            sh 'docker run -it --name apishkas --network="host" maslovu/api-tests'
        }
    }
  }

  stages {
    stage('Run Tests') {
      steps {
        sh 'pytest -s -v ApiTestsForMyrestAplic'
      }
    }

  }
}