import requests

def get_object_data(object_id):
    base_url = "https://api.restful-api.dev/objects"
    params = {'id': object_id}
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

def main():
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
