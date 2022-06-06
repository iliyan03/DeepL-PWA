import io
import json
import pyodide

class Translation:
    def __init__(self, data={}):
        self.translation = data.get('text')

def download_translation(text: str, target_lang: str) -> Translation:
    resp: io.StringIO = pyodide.open_url(f'/translation/data?text={text}&target_lang={target_lang}')
    translation = json.loads(resp.read())

    return Translation(data= translation)