from flask import Flask,render_template,jsonify
from database import load_jobs_form_db, load_job_by_id

app = Flask(__name__)

@app.route("/")
def hello():
  JOBS = load_jobs_form_db()
  return render_template('home.html',jobs = JOBS)

@app.route("/api/jobs")
def list_job():
  JOBS = load_jobs_form_db()
  return jsonify(JOBS)

@app.route("/job/<id>")
def show_job(id):
  job = load_job_by_id(id)
  if not job:
    return "Not Found",404
  return render_template('jobpage.html',job=job)


if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)