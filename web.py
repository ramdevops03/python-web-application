from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        selected_option = request.form['dropdown']
        return "You selected: {}".format(selected_option)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081
