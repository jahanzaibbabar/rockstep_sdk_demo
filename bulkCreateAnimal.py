import requests
from rockstep_sdk import RockStepAuth
from typing import List, Dict, Any


def bulk_create_animal(api_key: str, base_url: str, animal_data_list: Dict[str, List[Dict[str, Any]]])  -> str:
    """
    Create multiple animals using the RockStep API.

    Args:
        api_key (str): Your API key for authentication.
        base_url (str): The base URL of the RockStep API.
        animal_data_list (List[Dict[str, Union[int, str, List[Dict[str, Union[int, str]]]]]]): List of animal data for bulk creation.

    Returns:
        str: A message indicating the success or failure of the bulk animal creation.

    Raises:
        Exception: If there's an error during the API request.

    Example:
        # Example animal data list
        animal_data_list = [
            {
                "lineKey": 0,
                # ... (other fields) ...
            },
            # Add more dictionaries for each animal
        ]

        # Replace with your actual API key and base URL
        api_key = "your_api_key_here"
        base_url = "https://api.rockstep.com"

        # Call the bulk_create_animal function
        result = bulk_create_animal(api_key, base_url, animal_data_list)
        print(result)
    """

    
    # Initialize the SDK with your API key and base URL
    auth = RockStepAuth(api_key)

    # Define the endpoint URL
    endpoint = f"{base_url}/api/animals/bulkCreateAnimal"

    # Set up the headers for the POST request
    headers = auth.get_headers()
    headers["Content-Type"] = "application/json"

    try:
        # Send a POST request to create the animals
        response = requests.post(endpoint, headers=headers, json={"createAnimalRequestDtos": animal_data_list})

        if response.status_code == 201:
            return "Animals created successfully"
        else:
            return f"Failed to create animals: {response.status_code}"
    except Exception as e:
        return f"Error: {e}"
