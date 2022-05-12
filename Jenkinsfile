pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh 'echo "Hello bye bye"'
        sh '''
                    echo "Multiline shell steps works too"
                    ls -lah
                '''
      }
    }

    stage('stage3') {
      steps {
        withAnt(installation: '8', jdk: '8') {
          sleep 1
        }

        node(label: 'll') {
          sh 'sh'
          archiveArtifacts(allowEmptyArchive: true, artifacts: 'y')
          error 'Message'
        }

      }
    }

  }
  environment {
    t = 't'
  }
}