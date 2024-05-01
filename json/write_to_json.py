import json

def dump_json_to_file(json_object, filepath):
  """
  Dumps a JSON object to a file.

  Args:
      json_object (object): The JSON object to dump.
      filepath (str): The path to the output file.
  """
  with open(filepath, 'w') as f:
    json.dump(json_object, f, indent=4)  # Add indentation for readability (optional)

# Example usage
# dump_json_to_file(json_data, "output.json")
