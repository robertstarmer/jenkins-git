pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'env'
                sh 'echo "building hello world"'
            }
        }
        
        stage('Test') {
            steps {
                prop_readr = load 'helper.groovy'
                test1 = prop_readr.get_property("my_prop.properties")
                echo "got the propertie info: $test1"
                sh 'echo "Testing Hello World"'
                sh '''
                    echo "Multiline shell steps works too"
                    ls -lah
                '''
            }
        }
        
        stage('Deploy') {
            steps {
                sh 'echo "Deploying Hello World"'
            }
        }
        
    }
}
