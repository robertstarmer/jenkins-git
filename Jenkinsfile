pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'echo "Changing the project AGAIN"'
                sh '''
                    echo "Multiline shell steps works too"
                    ls -lah
                '''
            }
        }
    }
}
