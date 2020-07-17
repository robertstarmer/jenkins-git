pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'echo "Changing the project now"'
                sh '''
                    echo "Multiline shell steps works too"
                    ls -lah
                '''
            }
        }
    }
}
