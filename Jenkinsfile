pipeline {
    agent any
    stages {
        stage('Deploy') {
            steps {
                timeout(time: 1, unit: 'MINUTES') {
                    sh './fibonacci.sh 4'
                }
                timeout(time: 1, unit: 'MINUTES') {
                    sh './fibonacci.sh 8'
                }
            }
        }
    }
}
