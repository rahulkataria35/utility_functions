def find_key_paths(json_object, keys, path=""):
    key_paths = {}
    if isinstance(json_object, dict):
        for key, value in json_object.items():
            if key in keys:
                current_path = f"{path}.{key}" if path else key
                key_paths[key] = current_path
                key_paths.update(find_key_paths(value, keys, current_path))
            else:
                key_paths.update(find_key_paths(value, keys, f"{path}.{key}" if path else key))
    
    elif isinstance(json_object, list):
        for i, item in enumerate(json_object):
            key_paths.update(find_key_paths(item, keys, f"{path}[{i}]" if path else f"[{i}]"))
    return key_paths


# Example usage
json_data = {
  "customer": {
    "id": 12345,
    "name": "John Doe",  "email": "johndoe@example.com",  "phone_number": "+15551234567",  "address": {
      "street_address": "123 Main St",
      "city": "Anytown",
      "state": "CA",
      "zip_code": "12345"
    },
    "orders": [
      {
        "id": 100,
        "items": [
          {
            "product_id": "ABC123",
            "quantity": 2
          },
          {
            "product_id": "DEF456",
            "quantity": 1
          }
        ]
      },
      {
        "id": 200,
        "items": [
          {
            "product_id": "GHI789",
            "quantity": 1
          }
        ]
      }
    ]
  },
  "company": {
    "name": "Example Company",
    "website": "https://www.example.com"
  }
}


keys = ["email", "phone_number", "zip_code", "product_id"]
key_paths = find_key_paths(json_data, keys)
print(key_paths)