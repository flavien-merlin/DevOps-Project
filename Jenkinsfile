properties([pipelineTriggers([pollSCM('* * * * *')])])
node{

    stage("clone"){
        checkout([$class: 'GitSCM', branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/flavien-merlin/neo.git']]])
    }
    stage("Build"){
        sh "/usr/local/bin/docker-compose build"
    }
    stage("Run"){
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
            sh "/usr/local/bin/docker-compose push"
            sh "docker stop neo"   
        }
    }
}
