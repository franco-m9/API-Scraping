# Import requests for HTTP requests and pandas for table creation as a csv
import requests                                 
import pandas as pd                                              

# Initial API URL
baseurl = "https://rickandmortyapi.com/api/"
# Variable to append initial API URL directories
dir_character = "character"
# List to contain all the relevant data
mainlist = []

# Function that returns the status code of a URL
def status_code(url):
    response = requests.get(url)
    response = response.status_code
    return response

# Function that returns the Initial API URL appended with /character and /page # in JSON format
def main_request(baseurl, dir_character, x):
    response = requests.get(baseurl + dir_character + f'?page={x}')
    return response.json()

# Function that returns the total number of pages 
def get_pages(response):
    pages = response['info']['pages']
    return pages

# Function that defines a dictionary which contains the id, name, and total number of episodes they are in
def parse_json(response):
    charlist = []
    for item in response['results']:
        char = {
            'id': item['id'],
            'key': item['name'],
            'no_ep': len(item['episode']),
        }
        charlist.append(char)
    return charlist

# Main program which only runs on a successful status code (200)
if(status_code(baseurl)==200):
    print("Success. Status code of the API request is:", status_code(baseurl))
    data = main_request(baseurl, dir_character, 1)
    for x in range(1, get_pages(data)+1):
        mainlist.extend(parse_json(main_request(baseurl, dir_character, x)))
    df = pd.DataFrame(mainlist)
    df.to_csv('charlist.csv', index=False)
    print("Table complete. Please see the CSV file created")

# Main program returns an error and corresponding error code if not 200
else:
    print("Error. Status code of the API request is:", status_code(baseurl))
