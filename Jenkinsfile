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
    }
}
