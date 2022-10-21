# Christian Hart 001-68-3628

import requests
from dotenv import find_dotenv, load_dotenv
import os

load_dotenv(find_dotenv())

API_KEY = os.getenv("API_KEY")

# https://www.googleapis.com/books/v1/volumes?q=search+terms&key=(your-key)


def get_books(book):

    baseURL = "https://www.googleapis.com/books/v1/volumes?q="

    response = requests.get(
        "https://www.googleapis.com/books/v1/volumes",
        params={"q": book, "key": API_KEY}
    )

    response_json = (response.json())

    title = response_json["items"][0]["volumeInfo"]["title"]
    image = response_json["items"][0]["volumeInfo"]["imageLinks"]["thumbnail"]

    return [title, image]
