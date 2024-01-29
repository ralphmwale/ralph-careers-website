from flask import Flask, render_template
app = Flask(__name__) #how a particular script was invoked
@app.route("/") #part of the url that is accessed after the domain
def hello_ralph():
  return render_template('home.html')

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
