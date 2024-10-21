# This file creates a valid CPM compartmentalization descriptor in Python and prints it out.
# It can be toggled to create both weighted and unweighted variations.

import yaml

def write_cpm_format():

    # Set to true/false to add weights or not
    weighted = True
    
    # Define an empty compartmentalization
    c = {}
        
    #####  Object Map section  #####
    obj_map = []
    
    # Create two object domain definitions
    obj_descriptor1 = {}
    obj_descriptor1["name"] = "ObjectDomain1"
    obj_descriptor1["objects"] = ["main.c|global1", "main.c|global2", "main.c|global3"]
    
    obj_descriptor2 = {}
    obj_descriptor2["name"] = "ObjectDomain2"
    obj_descriptor2["objects"] = ["main.c|global4"]
    
    obj_map.append(obj_descriptor1)
    obj_map.append(obj_descriptor2)
    c["object_map"] = obj_map
    
    #####  Subject Map section  #####
    subj_map = []
    
    # Create two subject domain definitions
    subj_descriptor1 = {}
    subj_descriptor1["name"] = "SubjectDomain1"
    subj_descriptor1["subjects"] = ["main.c|main"]
    subj_descriptor2 = {}
    subj_descriptor2["name"] = "SubjectDomain2"
    subj_descriptor2["subjects"] = ["main.c|check_password"]
    
    subj_map.append(subj_descriptor1)
    subj_map.append(subj_descriptor2)
    c["subject_map"] = subj_map
    
    ##### Privileges section #####
    privileges = []
    
    # One privilege descriptor element
    privilege_descriptor = {}
    
    # Add some context to the privilege descriptor
    context_descriptor = {}
    context_descriptor["uid"] = "root"
    
    # Principal descriptor is a subject domain plus context
    principal_descriptor = {}
    principal_descriptor["subject"] = "SubjectDomain1"
    principal_descriptor["execution_context"] = context_descriptor
    privilege_descriptor["principal"] = principal_descriptor
    
    # Add some call/ret privileges in
    privilege_descriptor["can_call"] = ["SubjectDomain2"]
    privilege_descriptor["can_return"] = []
    
    # If weighted, add some call/return weights
    if weighted:
        privilege_descriptor["call_weights"] = [20]
        privilege_descriptor["return_weights"] = []
        
    # Read/write privileges 
    object_context_descriptor = {}
    object_context_descriptor["uid"] = "root"
    
    access_descriptor = {}
    access_descriptor["objects"] = ["ObjectDomain1", "ObjectDomain2"]
    if weighted:
        access_descriptor["weights"] = [11, 7]
        privilege_descriptor["can_read"] = [access_descriptor]

    access_descriptor = {}
    access_descriptor["objects"] = ["ObjectDomain1"]
    access_descriptor["object_context"] = object_context_descriptor
    privilege_descriptor["can_write"] = [access_descriptor]
    if weighted:
        access_descriptor["weights"] = [23]
    privileges.append(privilege_descriptor)

    c["privileges"] = privileges
    print(yaml.dump(c, sort_keys=False))

if __name__ == '__main__':
    write_cpm_format()
