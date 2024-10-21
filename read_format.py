import os
import sys
import yaml

# Read and print out a CPM IF file. Does not do sanity checking, eg that can_call and call_counts are the same length etc.
def read_cpm_format(filename):

    # Open file and parse as yaml. Save result in compartmentalization "c"
    file_stream = open(filename, "r")
    try:
        print("Loading yaml file...")
        c = yaml.safe_load(file_stream)
    except:
        print("Error parsing trace file " + filename)

    # Print out the subject map
    print("subject map:")
    for subj_domain in c["subject_map"]:
        sd_name = subj_domain["name"]
        subjects = subj_domain["subjects"]
        print(sd_name + "\n\t" + str(subjects))

    # Print out the object map
    print("object map:")
    for obj_domain in c["object_map"]:
        od_name = obj_domain["name"]
        objects = obj_domain["objects"]
        print(od_name + "\n\t" + str(objects))

    # Print out the privileges
    print("Privileges:")
    for priv in c["privileges"]:

        # Read header with principal info
        principal = priv["principal"]
        subject = principal["subject"]
        execution_context = principal.get("execution_context", {})

        print("principal:")
        print("\tsubject: " + subject)
        print("\texecution_context: " + str(execution_context))

        # Read call/return privileges
        can_call = priv.get("can_call", [])
        call_counts = priv.get("call_counts", [])
        can_return = priv.get("can_return", [])
        return_counts = priv.get("return_counts", [])

        print("\tcan_call: " + str(can_call))
        if len(call_counts) > 0:
            print("\tcall_counts: " + str(call_counts))
        print("\tcan_return: " + str(can_return))
        if len(return_counts) > 0:
            print("\treturn_counts: " + str(return_counts))

        # Read read/write privileges
        print("\tcan_read:")
        for read_access in priv["can_read"]:
            objs = read_access.get("objects", [])
            object_context = read_access.get("object_context", {})
            print("\t\tobjects: " + str(objs))
            print("\t\tobject_context: " + str(object_context))

        print("\tcan_write:")            
        for write_access in priv["can_write"]:
            objs = read_access.get("objects", [])
            object_context = read_access.get("object_context", {})
            print("\t\tobjects: " + str(objs))
            print("\t\tobject_context: " + str(object_context))

if __name__ == '__main__':
    args = sys.argv
    if len(args) != 2:
        raise Exception("Usage: read_format.py <input-yaml>")
    read_cpm_format(sys.argv[1])
