import json

def pretty_print_json(json_object):
  """
  Pretty-prints a JSON object for better readability.

  Args:
      json_object (object): The JSON object to print.
  """
  print(json.dumps(json_object, indent=4))

# Example usage
pretty_print_json(json_data)
