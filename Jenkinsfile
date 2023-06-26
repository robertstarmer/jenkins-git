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
                script {
                    J_FILENAME = "new_output.json"
                    def prop_readr = load "helper.groovy"
                    test1 = prop_readr.get_property("my_prop.properties")
                    sh label: "run python file", script: "python3 my_python.py $J_FILENAME"
                    def json_content = readFile(file: J_FILENAME)
                    echo "json content is $json_content"
                    // def jsonContent = readJSON text: jsonFile
                }
                echo "got the propertie info: $test1"
                sh 'echo "Testing Hello World"'
                sh label: "get env", script: "env"
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
