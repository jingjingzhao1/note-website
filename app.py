from flask import Flask,render_template,jsonify

app = Flask(__name__)

JOBS = [
  {
    'id':1,
    'title':'Web Developer',
    'location':'Remote',
    'salary':'Up to $80,000 a year - Full-time'
  },
  {
    'id':2,
    'title':'Software Engineer/Developer (Desktop)',
    'location':'Portland OR',
    'salary':'$73,983 - $166,365 a year - Full-time'
  },
  {
    'id':3,
    'title':'Remote Software Support Engineer',
    'location':'Remote',
    'salary':'$83,000 - $115,000 a year'
  },
  {
    'id':4,
    'title':'Principal Engineer or Senior Principal Engineer Software - DevOps',
    'location':'El Segundo, CA',
    'salary':''
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