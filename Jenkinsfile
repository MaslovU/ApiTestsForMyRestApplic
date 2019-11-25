 
pipeline {
      agent any
  
  stages {

    stage ('run docker') {
      steps {
        sh 'docker run --network="host" maslov/api-tests'
      }
    }
    
    stage('run tests') {
      steps {
        sh 'pytest -s -v Test_Api_Rest_Aplic'
      }
    }
  }
}
