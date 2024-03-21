# import requests
# from app import app

# # Define the base URL and parameters
# base_url = 'https://goodfoods-search-grocery-product-reviews-by-barcode-v1.p.rapidapi.com/search'
# params = {'barcode': '823734014026'}
# headers = {
#     'X-RapidAPI-Key': '04e4815de3msh8f398e0ef7df3cbp182918jsna1791a044dc9',
#     'X-RapidAPI-Host': 'goodfoods-search-grocery-product-reviews-by-barcode-v1.p.rapidapi.com'
# }

# try:
#     # Send the GET request using requests library
#     response = requests.get(base_url, params=params, headers=headers)
#     response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
#     product_data = response.json()
#     print(product_data)  # Output the response data
# except requests.exceptions.RequestException as e:
#     # Handle request errors
#     print("Error:", e)
