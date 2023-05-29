"""
Provides the server for language translator
"""

from flask import Flask, render_template, request
from machinetranslation import translator


app = Flask("Web Translator")

@app.route("/englishToFrench")
def english_to_french():
    """implement api for translating english to french."""
    text_to_translate = request.args.get('textToTranslate')
    # Write your code here
    return translator.english_to_french(text_to_translate)

@app.route("/frenchToEnglish")
def french_to_english():
    """implement api for translating french to english."""
    text_to_translate = request.args.get('textToTranslate')
    # Write your code here
    return translator.french_to_english(text_to_translate)

@app.route("/")
def render_index_page():
    """implement  index html."""
    # Write the code to render template
    return "this is the index page"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
