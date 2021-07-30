#import a library
from re import DEBUG
from flask import Flask, render_template, request
import joblib

# instance of an app
app = Flask(__name__)

model=joblib.load('dib_79.pkl')

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/blog', methods=['POST'])
def contact():
    a = request.form.get('preg')
    b = request.form.get('plas')
    c = request.form.get('pres')
    d = request.form.get('skin')
    e = request.form.get('test')
    f = request.form.get('mass')
    g = request.form.get('pedi')
    h = request.form.get('age')
 
    pred=model.predict([[int(a),int(b),int(c),int(d),int(e),int(f),int(g),int(h)]])

    if pred[0]==1:
        output='Diabetic'
    else:
        output='Not diabetic'

    return render_template('blog.html', predicted_text=f'The person is {output}')

@app.route('/test')
def test():
    return 'Just for testing'

# run the app
if __name__ =='__main__':
    app.run(debug=True)  # Debug=True will run terminal automatically
