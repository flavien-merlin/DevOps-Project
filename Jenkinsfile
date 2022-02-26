properties([pipelineTriggers([pollSCM('* * * * *')])])
pipeline{
    environment{
        registry = "flav95/neo" 
        registryCredential = 'neo-dockerhub'
    }

        stage("clone"){
            checkout([$class: 'GitSCM', branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/flavien-merlin/neo.git']]])
        }
        stage("Build & Run"){
            sh "/usr/local/bin/docker-compose up -d"
        }
        stage("Test"){
            try{
                sh "python3 /Users/neo/.jenkins/workspace/neo-wog/e2e.py"
            }
            catch (error){
                sh "echo Jenkins failed"
            }
        }
        stage("Finalize"){
            steps{
                   script{
                    docker.withRegistry( '', registryCredential ) {
                        dockerImage.push()
                    }
                } 
            }
            steps{
            sh "docker stop neo"   
            }
        }
        post{
            always{
                sh "docker logout"
            }
        }
}
