properties([pipelineTriggers([pollSCM('* * * * *')])])
node {
    environment{
        DOCKERHUB_CREDENTIALS = credentials('neo-dockerhub')
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
    stage("Login to docker-hub"){
        sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
    }
    stage("Finalize"){
        steps{
            sh 'docker push flav95/neo-alpine:latest'
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
