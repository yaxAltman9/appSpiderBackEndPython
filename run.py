from app import create_app
from app.models import JobModel
from flask_mysqldb import MySQL

app = create_app()

# 初始化 MySQL 和 JobModel
mysql = MySQL(app)
job_model = JobModel(mysql)
app.config['JOB_MODEL'] = job_model

if __name__ == '__main__':
    app.run(port=3000)
