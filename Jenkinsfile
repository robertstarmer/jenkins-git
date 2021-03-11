pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'echo "Hello World"'
            }
        }
        stage('Do some work') {
            steps {
                sh '''
                    echo "Multiline shell steps works too"
                    ls -lah
                '''
            }
        }
        stage('Show disc space') {
            steps {
                sh '''
                    echo "Displaying drive space"
                    df -h
                ...
            }
        }
    }
}
