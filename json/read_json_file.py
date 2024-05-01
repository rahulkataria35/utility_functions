import json

def load_json_from_file(filepath):
  """
  Loads a JSON object from a file.

  Args:
      filepath (str): The path to the JSON file.

  Returns:
      object: The parsed JSON object.
  """
  with open(filepath, 'r') as f:
    return json.load(f)

# Example usage
# json_data = load_json_from_file("data.json")
