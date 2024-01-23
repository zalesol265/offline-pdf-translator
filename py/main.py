from flask import Flask, redirect, url_for, request, jsonify
from flask_cors import CORS

from translation import argos_translate, download_argos_language, get_available_languages, get_installed_languages

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})

 
@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()
    tranlsated_text = argos_translate(data['text'], data['input_lang'], data['output_lang'])
    return jsonify(tranlsated_text)


@app.route('/languages')
def languages():
    language_list = get_available_languages()
    return jsonify(language_list)


@app.route('/installed')
def installed_languages():
    language_list = get_installed_languages()
    return jsonify(language_list)



@app.route('/success/<name>')
def success(name):
    return jsonify('welcome %s' % name )
 
 
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))
 
 
if __name__ == '__main__':
    app.run(debug=True)