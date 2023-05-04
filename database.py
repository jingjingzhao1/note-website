from sqlalchemy import create_engine,text,insert
import os

db_connect_info = os.environ['DB_CON_STR']


engine = create_engine(db_connect_info,
                       connect_args={
                         "ssl":{
                           "ssl_ca": "/etc/ssl/cert.pem"
                         }
                       }
                      
                      )


def load_jobs_form_db():
  with engine.connect() as connection:
    result = connection.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(row._mapping)
    return jobs


def load_job_by_id(idx):
  with engine.connect() as connection:
    result = connection.execute(text("select * from jobs where id = :val"),dict(val=idx))
    rows = result.all()
    if(len(rows) == 0):
      return None
    else:
      return rows[0]._mapping
    

def add_appl_to_job(job_id,data):
   with engine.connect() as connection:
    query = text("insert into applications(job_id,full_name,email,experience) values(:job_id,:full_name,:email,:experience)")

    connection.execute(query,
                       {
                         'job_id':job_id,
                         'full_name':data['full_name'],
                         'email':data['email'],
                         'experience':data['experience']
                       })
                       

                               