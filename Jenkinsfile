pipeline {
  
  agent any
  
  stages {
    stage ('run docker') {
      steps {
        sh 'docker run --network="host" maslovu/api-tests'
      }
    }
    stage('run test') {
      steps {
        sh "docker exec -it apishkas 'pytest -s -v ApiTestsForMyrestAplic'"
      }
    }

  }
}
