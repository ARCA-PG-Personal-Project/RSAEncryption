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
                    docker.build('your_image_name:1', '-f Dockerfile .')
                }
		}
            }
        }

	stage("Install kubectl"){
            steps {
                sh """
                    curl -LO https://storage.googleapis.com/kubernetes-release/release/v1.23.6/bin/linux/amd64/kubectl
                    chmod +x ./kubectl
                    ./kubectl version --client
                """
		
            }
        }
	
        stage('Deploy to Kubernetes') {
            steps {
		
                script {
                    // Deploy the Kubernetes manifests
		    sh "aws eks update-kubeconfig --region eu-west-1 --name $CLUSTERID"
                    sh 'kubectl apply -f deployment.yaml -n rsa-service'
                    sh 'kubectl apply -f service.yaml -n rsa-service'
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

