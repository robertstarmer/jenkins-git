def get_property(String prop_file){
    echo "reading file $prop_file"
    prop = readProperties file:prop_file
    echo "returning prop.TEST_1: $prop.TEST_1"
    String ret = "NOTHING"
    if (prop?.TEST_1){
        ret = "$prop.TEST_1"
    }

    return ret
}

def check_env() {
    sh label: "check env", script: "env"
}

return this
