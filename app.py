from flask import Flask,render_template,jsonify

app = Flask(__name__)

JOBS = [
  {
    'id':1,
    'title':'title',
    'location':'location',
    'salary':'$$$$'
  },
  {
    'id':2,
    'title':'title2',
    'location':'location2',
    'salary':'$$$$2'
  },
  {
    'id':3,
    'title':'title3',
    'location':'location3',
    'salary':'$$$$3'
  }

]


@app.route("/")
def hello():
  return render_template('home.html',jobs = JOBS)

@app.route("/api/jobs")
def list_job():
  return jsonify(JOBS)
  
if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)