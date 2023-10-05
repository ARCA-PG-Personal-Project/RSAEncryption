pipeline {
    agent any
    
    environment {
        SERVICE_NAME = "rsa-encryption-service"
        ORGANIZATION_NAME = "arca-pg-personal-project"
        DOCKERHUB_USERNAME = "frankisinfotech"
	REPOSITORY_TAG = "${DOCKERHUB_USERNAME}/${ORGANIZATION_NAME}-${SERVICE_NAME}:${BUILD_ID}"
    }
    
    stages {
        stage('Build') {
            steps {
		withDockerRegistry([credentialsId: 'docker-hub', url: ""]){
                script {
                    // Build the Docker image
                    sh 'docker build -t ${REPOSITORY_TAG} .'
		    sh 'docker push ${REPOSITORY_TAG}'
                }
		}
            }
        }


	
        stage('Deploy to Kubernetes') {
            steps {
		
                script {
                    // Deploy the Kubernetes manifests
		    sh "aws eks update-kubeconfig --region eu-west-1 --name $CLUSTERID"
                    sh '$kubectl apply -f deployment.yaml -n arca-payment-service'
                    sh '$kubectl apply -f service.yaml -n arca-payment-service'
                }
            }
        }
	stage('Remove Unused docker image') {
          steps{
            script {
             
              sh "docker system prune -f"
                    }
                }
        }
    }

    
}

