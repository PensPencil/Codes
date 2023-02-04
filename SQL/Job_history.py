import sqlite3

conn = sqlite3.connect('job_history.db')

conn.execute('''CREATE TABLE IF NOT EXISTS job_history(
    employee_id VARCHAR(20) NOT NULL, 
    start_date datetime,
    end_date datetime, 
    job_id VARCHAR(20),
    department_id VARCHAR(20),
    FOREIGN KEY (job_id) REFERENCES Job(job_id)
);            
''')

conn.execute('''CREATE TABLE IF NOT EXISTS Job(
    job_id VARCHAR(20) PRIMARY KEY NOT NULL,
    job_title TEXT NOT NULL,
    Min_salary INTEGER NOT NULL,
    Max_salary INTEGER NOT NULL
);
''')

conn.execute('''INSERT INTO job_history(employee_id, start_date, end_date, job_id, department_id)
      VALUES('H64JK497', '2-12-2019', '2-02-2022', '7AK56F', 'HKJRGI98'),
            ('H68JK497', '1-11-2017', '1-04-2022', 'KHKJ67', 'HUI768GV'),
            ('HIUVDR87', '2-01-2015', '2-02-2021', 'JH624', 'HFEK6789'),
            ('JGFE8648', '11-01-2016','10-02-2022','IFR87', 'HUERIY99'),
            ('FHUER455', '5-04-2014','11-01-2011','6478F', 'HRU367HJ');
''')
conn.execute('''INSERT INTO Job(job_id, job_title, Min_salary, Max_salary)
      VALUES('7AK56F','Real estate agent', 500000, 900000),
            ('KHKJ67', 'Computer programmer', 7000000, 100000000),
            ('JH624', 'Teacher', 5000000, 20000000),
            ('IFR8', 'Veterinarian', 800000, 100000000),
            ('6478F', 'Accountant', 3000000, 200000000);
''')

query = "SELECT * FROM job_history, Job WHERE job_history.job_id=Job.job_id"
for i in conn.execute(query):
    print(i)
