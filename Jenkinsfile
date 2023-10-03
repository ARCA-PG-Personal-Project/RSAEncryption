pipeline {
    agent any
    
    environment {
        SERVICE_NAME = "rsa-encryption-service"
        ORGANIZATION_NAME = "arca-pg-personal-project"
        DOCKERHUB_USERNAME = "frankisinfotech"
	composeFile = "docker-compose.yml"
	REPOSITORY_TAG = "${DOCKERHUB_USERNAME}/${ORGANIZATION_NAME}-${SERVICE_NAME}:${BUILD_ID}"
    }
    
    stages {
//         stage ('Preparing') {
//             steps {
//                 cleanWs()
//                 git credentialsId: 'Github', url: "git@github.com:wasp-networks/Arca.UserManagement.git" //${ORGANIZATION_NAME}/${SERVICE_NAME}"
//             }
//         }
        
        stage ('Build and Push Image') {
            steps {
                 withDockerRegistry([credentialsId: 'docker-hub', url: ""]) {
                   // sh 'docker build -t ${REPOSITORY_TAG} --build-arg DBHOST="$DBHOST" --build-arg DBUSER="$DBUSER" --build-arg DBPASSWORD="$DBPASSWORD"  --build-arg AGENCYDATABASE="$AGENCYDATABASE" .'
                    sh 'docker build -t ${REPOSITORY_TAG} .'
		    sh 'docker push ${REPOSITORY_TAG}'             
		  //sh 'docker tag rsaencryption-web:1 frankisinfotech/arca-pg-personal-project-rsaencryption-web:1.0'
		  //  sh 'docker-compose push' // frankisinfotech/rsaencryption-web:1.0' //-f ${composeFile}  up -d"
	          //  sh 'docker-compose up -d'
	           
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


        
        stage ('Deploy to Cluster') {
            steps {
                sh "aws eks update-kubeconfig --region eu-west-1 --name $CLUSTERID"
                sh " envsubst < ${WORKSPACE}/deploy.yaml | ./kubectl apply -f - "
            }
       
        }

        stage('Remove Unused docker image') {
          steps{
            script {
             // sh "docker rmi -f  ${IMAGE_REPO_NAME}:${IMAGE_TAG} ${REPOSITORY_URI}:$IMAGE_TAG"
              sh "docker system prune -f"
                    }
                }
            }

    }
}

