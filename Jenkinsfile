pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'echo "Disabling the auto run option"'
                sh '''
                    echo "Multiline shell steps works too"
                    ls -lah
                '''
            }
        }
    }
}
