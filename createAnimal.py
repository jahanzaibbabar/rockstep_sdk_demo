import requests
from rockstep_sdk import RockStepAuth

def create_animal(api_key: str, base_url: str, animal_data: dict) -> str:
    """
    Create an animal using the RockStep API.

    Args:
    api_key (str): Your API key for authentication.
    base_url (str): The base URL of the RockStep API.
    animal_data (dict): Data for the animal to be created.

    Returns:
    str: A message indicating the success or failure of the animal creation.

    Raises:
    Exception: If there's an error during the API request.

    Example:
    # Example animal data
    animal_data = {
    "lineKey": 0,
    # ... (other fields) ...
    }

    # Replace with your actual API key and base URL
    api_key = "your_api_key_here"
    base_url = "https://api.rockstep.com"

    # Call the create_animal function
    result = create_animal(api_key, base_url, animal_data)
    print(result)
    """
    # Initialize the SDK with your API key and base URL
    auth = RockStepAuth(api_key)

    # Define the endpoint URL
    endpoint = f"{base_url}/api/animals/createAnimal"

    # Set up the headers for the POST request
    headers = auth.get_headers()
    headers["Content-Type"] = "application/json"

    try:
    # Send a POST request to create the animal
        response = requests.post(endpoint, headers=headers, json=animal_data)

        if response.status_code == 201:
            return "Animal created successfully"
        else:
            return f"Failed to create animal: {response.status_code}"
    except Exception as e:
        return f"Error: {e}"