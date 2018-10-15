import requests
import re
import time

ARTIST_API = 'https://www.vagalume.com.br'
INDEX = '/index.js'

API_URL = 'https://api.vagalume.com.br'
API_LYRIC_SEARCH_URL = API_URL + '/search.php'

WAIT_TIME_SEC = 5


class Artist(object):
    def __init__(self, artist_name=None):
        self.change_artist(artist_name)
    
    def change_artist(self, name):
        response = requests.get(ARTIST_API+'/'+name+INDEX)
        artist = response.json()
        self.id = artist['artist']['id']
        self.url = artist['artist']['url'] 
        self.lyrics_list = artist['artist']['lyrics']['item']
        self.name = name
        return response
    
    def get_lyrics_text_by_id(self, mus_id):
        params = {
            'art': self.name,
            'musid': mus_id
        }
        response = requests.get(API_LYRIC_SEARCH_URL, params=params)
        response.raise_for_status()
        return response.json()['mus'][0]['text']

    def get_lyrics_text_by_name(self, mus_name):
        params = {
            'art': self.name,
            'musid': mus_name
        }
        response = requests.get(API_LYRIC_SEARCH_URL, params=params)
        response.raise_for_status()
        return response.json()['mus'][0]['text']
    
    def get_all_lyrics_texts(self):
        for lyrics in self.lyrics_list:
            if 'text' not in lyrics:
                while True:
                    try:
                        text = self.get_lyrics_text_by_id(mus_id = lyrics['id'])
                    except Exception as e:
                        print('Failed request: ', e)
                        print('Retrying in ', WAIT_TIME_SEC, ' secs')
                        time.sleep(WAIT_TIME_SEC)
                        continue
                    break
                lyrics['text'] = text
                print('Finished song with id: ', lyrics['id'])
        return True
            
    
