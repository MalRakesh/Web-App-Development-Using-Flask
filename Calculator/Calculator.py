from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = ''
    if request.method == 'POST':
        try:
            expression = request.form.get('expression')
            # Evaluate the expression safely
            result = eval(expression, {"__builtins__": None}, {})
        except Exception as e:
            result = f'Error: {e}'
    return render_template('Calculator.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
