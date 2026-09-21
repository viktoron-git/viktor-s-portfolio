from flask import Flask, render_template, redirect



app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('aboutme.html')

@app.route('/projects')
def my_projects():

    return render_template('projects.html')

@app.route('/contact')
def contact_me():
    return render_template('contactme.html')



if __name__ == '__main__':
    app.run(debug=True)


