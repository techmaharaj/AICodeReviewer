import requests

def get_object_data(object_id):
     """
    Fetch data for the object with the given ID from the API.

    Parameters:
        object_id (str): The ID of the object to fetch.

    Returns:
        dict: The object data if the request is successful.
        None: If the request fails or no data is found.
    """
    base_url = "https://api.restful-api.dev/objects"
    params = {'id': object_id}

    try:
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching the data: {e}")
        return None

def main():
    """
    Main function to prompt the user for an object ID and print the object data.
    """
    object_id = input("Enter the object ID: ")
    
    object_data = get_object_data(object_id)
    if object_data and isinstance(object_data, list) and len(object_data) > 0:
        obj = object_data[0]
        print("Object Data:")
        print(f"ID: {obj['id']}")
        print(f"Name: {obj['name']}")
    else:
        print("Failed to retrieve the data or no data found.")

if __name__ == "__main__":
    main()
