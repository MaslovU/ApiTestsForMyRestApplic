pipeline {
  agent { label 'maslovu/api-tests'}
  
  stages {
    stage("docker run") {
      steps {
        sh 'docker run -it --name apishkas --network='host' maslov/api-tests'
      }
    }
    
    stage('run tests') {
      steps {
        sh 'pytest -s -v ApiTestsForMyrestAplic'
      }
    }

  }
}
