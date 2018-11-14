from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('maps.html')

@app.route('/my-link/')
def my_link():
  return 'Click.'

@app.route('/january/')
def january():
  return 'Click.'

if __name__ == '__main__':
  app.run(debug=True)
