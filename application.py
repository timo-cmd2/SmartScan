from flask import Flask
from flask import render_template
app = flask(__name__)


@app.route('/')
@app.route("/home")

def home:
  return render_template('home.html', title = SmartScan)

if __name__ == '__main__':
  app.run(debug = true)
