import yaml
import jsonschema
import sys

def load_yaml(file_path):
    """Load a YAML file."""
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def load_schema(schema_path="cpm_if_schema.yaml"):
    """Load the CPM schema from a file."""
    with open(schema_path, 'r') as file:
        return yaml.safe_load(file)

def validate_yaml(file_path, schema_path="cpm_if_schema.yaml"):
    """Validate a given YAML file against the schema."""
    try:
        data = load_yaml(file_path)
        schema = load_schema(schema_path)
        jsonschema.validate(instance=data, schema=schema)
        print(f"{file_path} is valid according to the schema.")
    except jsonschema.exceptions.ValidationError as e:
        print(f"Validation error in {file_path}: {e.message}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python validate_cpm_yaml.py <file.yaml>")
    else:
        validate_yaml(sys.argv[1])
