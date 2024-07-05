import requests

BASE_URL = "http://your-fastapi-url/api"

def get_regions_data():
    response = requests.get(f"{BASE_URL}/regions")
    return response.json()

def get_department_data(region_id):
    response = requests.get(f"{BASE_URL}/regions/{region_id}/departments")
    return response.json()

def get_city_data(department_id):
    response = requests.get(f"{BASE_URL}/departments/{department_id}/cities")
    return response.json()
