pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'echo "Changing the project Uno more"'
                sh '''
                    echo "Multiline shell steps works too"
                    ls -lah
                '''
            }
        }
    }
}
