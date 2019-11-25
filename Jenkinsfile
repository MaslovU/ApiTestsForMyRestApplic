pipeline {
  
  agent any
  
  stages {
    stage ('run docker') {
      steps {
        sh 'docker start jenka'
        sh "docker exec jenka 'pytest -s -v ApiTestsForMyrestAplic'"
      }
    }

  }
}
