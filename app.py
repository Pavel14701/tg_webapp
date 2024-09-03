from flask import Flask, render_template
from turbo_flask import Turbo

app = Flask(__name__)
turbo = Turbo(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/update')
def update():
    dynamic_data = "Updated data"
    return turbo.stream(turbo.append(dynamic_data, target='dynamic-data'))

if __name__ == '__main__':
    app.run(debug=True)