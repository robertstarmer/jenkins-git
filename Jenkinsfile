pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'echo "It works!!!!!!!"'
                sh '''
                    echo "Multiline shell steps works too"
                    ls -lah
                '''
            }
        }
    }
}
