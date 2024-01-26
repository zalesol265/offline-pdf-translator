from flask import Flask, redirect, url_for, request, jsonify
from flask_cors import CORS

from translation import argos_translate, download_argos_language, get_available_languages, get_installed_languages
from convertDocs import convert_pdf_to_docx, download_file, translate_text

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
 
 
@app.route('/documentTranslate', methods=['POST'])
def translate_files():
    try:
        if 'file' in request.files:
            pdf_file = request.files['file']
            input_lang = request.form.get('input_lang')
            output_lang = request.form.get('output_lang')
            
            pdf_filename = "temp.pdf"
            pdf_file.save(pdf_filename)
            docx_file = convert_pdf_to_docx(pdf_filename, pdf_file.filename)
            translated_docx_file = translate_text(docx_file, input_lang, output_lang)
            download_file(translated_docx_file)

            return jsonify({'success': True, 'docx_path': translated_docx_file}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True)