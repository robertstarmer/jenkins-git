pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'echo "THIS should come from a PR"'
                sh '''
                    echo "Multiline shell steps works too"
                    ls -lah
                '''
            }
        }
    }
}
