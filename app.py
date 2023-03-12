import os
import openai
from flask import Flask, render_template, request
import time

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def process_text():
    if request.method == 'POST':
        key = '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'
        openai.api_key = key
        input_text = request.form['input_text']
        try:
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=f"Correct this to formal English: {input_text}",
                temperature=0,
                max_tokens=60,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0
            )
            output_text = response['choices'][-1]['text']
        except openai.error.APIError as e:
            error_message = str(e)
            return render_template('index.html', error_message=error_message)
        
        return render_template('index.html', output_text=output_text)
    
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)
