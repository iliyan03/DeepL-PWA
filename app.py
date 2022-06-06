import flask, deepl

auth_key = '71a12331-f0d0-d9de-da46-1a6527d7af34:fx'
translator = deepl.Translator(auth_key)

app = flask.Flask(__name__)

@app.route("/")
def index():
    return flask.render_template('index.html')

@app.route('/translation/data')
def translation():
    text_to_translate: str = flask.request.args.get('text')
    target_lang: str = flask.request.args.get('target_lang')
    
    data = {'text': translator.translate_text(text_to_translate, target_lang=target_lang).text}

    return flask.jsonify(data)

@app.route('/serviceWorker.js')
def sw():
    response = flask.make_response(
        flask.send_from_directory(
            'static', '/', filename='serviceWorker.js'
        )
    )
    #change the content header file. Can also omit; flask will handle correctly.
    response.headers['Content-Type'] = 'application/javascript'
    return response