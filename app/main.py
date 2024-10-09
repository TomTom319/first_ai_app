from flask import Flask, request, render_template
from preprocess import preprocess_text
from generate import generate_microcontent

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_content = request.form['content']
        processed_content = preprocess_text(user_content)

        #generate content
        microcontent = generate_microcontent(user_content)

        return f"Processed Content: {processed_content}<br>Generated Microcontent: {microcontent}"
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)