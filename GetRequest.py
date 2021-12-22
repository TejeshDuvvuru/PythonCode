#  pip install requests
# import the request library
import requests
import configparser
config = configparser.RawConfigParser()
config.read('ConfigFile.properties')
url = config.get("GetApi", "url")

# data = []

try:
    # post_data = requests.post(url, data_to_be_post)
    response = requests.get(url)

except Exception as error:
    print("Error in exception:", error)
finally:
    print("finnal response",response)