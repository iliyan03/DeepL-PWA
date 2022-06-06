from deepl_api import download_translation

from js import DOMParser, document, setInterval, console

def main():
    add_translate_event()

def translate(text: str, target_lang: str):
    translation = download_translation(text= text, target_lang= target_lang).translation
    document.getElementById('translated_text').innerHTML = translation

def add_translate_event():
    def evt(e= None):
        translate(
            text = document.getElementById('text_to_translate').value,
            target_lang = 'BG'
            )
        if e:
            e.preventDefault()
        return False
    
    translate_btn = document.getElementById('translate_btn')
    translate_btn.onclick = evt

try:
    main()
except Exception as x:
    print(f"Error starting translation script: {x}")