def get_property(String prop_file){
    prop = readProperties file:prop_file
    return $prop.TEST_1
}

return this
