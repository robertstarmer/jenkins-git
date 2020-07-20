pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'echo "One more change, just to make sure it works locally"'
                sh '''
                    echo "Multiline shell steps works too"
                    ls -lah
                '''
            }
        }
    }
}
