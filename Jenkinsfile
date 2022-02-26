properties([pipelineTriggers([pollSCM('* * * * *')])])
node {  
    stage("clone"){
        checkout([$class: 'GitSCM', branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/flavien-merlin/neo.git']]])
    }
    stage("Build & Run"){
        sh "/usr/local/bin/docker-compose up -d"
    }
    stage("Test"){
        try{
            sh "python3 e2e.py"
        }
        catch (error){
            sh "echo Jenkins failed"
        }
    }
    stage("Finalize"){
        steps{
             withDockerRegistry([ credentialsId: "neo-dockerhub", url: "" ])
        }
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
