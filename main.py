import os
from dotenv import load_dotenv
import requests



if __name__ == '__main__':
    load_dotenv()
    api_key = os.getenv('API_KEY')
    print(api_key)

    username = "primitivetechnology9550"
    url = f"https://www.googleapis.com/youtube/v3/channels?part=id&forUsername={username}&key={api_key}"
    response = requests.get(url)
    data = response.json()
    print(data)

    # channel_ids = [
    #     'UC-OVMPlMA3-YCIeg4z5z23A', # moscowpython
    #     'UCwHL6WHUarjGfUM_586me8w', # highload
    # ]

    # data = get_youtube_data(api_key, channel_ids)
