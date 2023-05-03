from sqlalchemy import create_engine,text
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