import json

def merge_json_objects(dict1, dict2):
  """
  Merges two dictionaries recursively, with values from dict2 overriding
  those in dict1 for duplicate keys.

  Args:
      dict1 (dict): The first dictionary.
      dict2 (dict): The second dictionary.

  Returns:
      dict: The merged dictionary.
  """
  result = dict1.copy()
  
  for key, value in dict2.items():
    if isinstance(value, dict) and key in result:
      result[key] = merge_json_objects(result[key], value)
    else:
      result[key] = value
  return result

# Example usage
merged_data = merge_json_objects(json_data, {"company": {"slogan": "We are the best!"}})
