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
                    sh label: "run python file", script: "python3 my_python.py -mos_tasks_filename $J_FILENAME"
                    def json_content = readFile(file: J_FILENAME)
                    archiveSingleFile(J_FILENAME, false)
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

def archiveSingleFile(String file_path, Bool track_file){
     sh label: "check current path", script: "pwd;"
    if (!fileExists(file_path)) {
        echo "ERROR: try to archive: $file_path but it does not exist."
        return
    }
    archiveArtifacts "$file_path", fingerprint: track_file
}