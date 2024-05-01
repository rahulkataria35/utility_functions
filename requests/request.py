import json
import requests


def service_function(method, payload, url, headers, params=None, data=None, files=None, timeout=10):
    try:
        if method.upper() == "GET":
            response = requests.get(url, headers=headers, params=params, timeout=timeout)
        
        elif method.upper() == "POST":
            response = requests.post(url, headers=headers, json=payload, data=data, files=files, timeout=timeout)
        
        elif method.upper() == "PUT":
            response = requests.put(url, headers=headers, json=payload, data=data, timeout=timeout)
        
        elif method.upper() == "DELETE":
            response = requests.delete(url, headers=headers, timeout=timeout)
        
        else:
            error = {"error": "Invalid HTTP method"}
            return error
        
        response.raise_for_status() # Raise an exception for non-200 status codes
        return response.json()
    
    except requests.exceptions.RequestException as e:
        error = {"error": "unable to parse data from response",
                 "data": str(e)}
        return error
    
    except json.JSONDecodeError as e:
        error = {"error": "unable to parse data from response",
                 "data": str(e)}
        return error