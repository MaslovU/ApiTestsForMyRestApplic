pipeline {
	agent {
		docker {image "maslovu/api-tests"}
	}
	stages {

        	stage('Pytest') {
            		steps {
                		sh "pytest -s -v ApiTestsForMyrestAplic"
            		}
        	}
	}
}