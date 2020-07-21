pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'echo "This should come from a PR"'
                sh '''
                    echo "Multiline shell steps works too"
                    ls -lah
                '''
            }
        }
    }
}
