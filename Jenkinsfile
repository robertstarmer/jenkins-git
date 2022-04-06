pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'echo "Hello!-PPP"'
                sh '''
                    echo "Multiline shell steps works too"
                    ls -lah
                '''
            }
        }
    }
}
