pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'echo "Hello!!"'
                sh '''
                    echo "Multiline shell steps works too"
                    ls -lah
                '''
            }
        }
    }
}
