import requests


def download(url, file_name):
    with open(file_name, "wb") as file:  # open in binary mode
        response = requests.get(url)  # get request
        file.write(response.content)  # write to file