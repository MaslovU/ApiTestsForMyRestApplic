pipeline {
  agent { dockerfile true }
  stages {
    stage('run tests') {
      steps {
        sh 'pytest -s -v ApiTestsForMyrestAplic'
      }
    }
  }
}
