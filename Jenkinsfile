 
pipeline {
 agent {
  docker {
   image ('maslovu/api-tests')
  }
 }
  
  stages {

    stage ('run tests') {
      steps {
       sh "docker exec -it maslovu/api-tests 'pytest -s -v Test_Api_Rest_Aplic'"
      }
    }
  }
}
