properties([pipelineTriggers([pollSCM('*/30 * * * *')])])
node {
    stage("clone"){
        checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/flavien-merlin/neo.git']]])
    }
    stage("Build"){
        sh "/usr/local/bin/docker-compose up"
    }
    
    }
}
