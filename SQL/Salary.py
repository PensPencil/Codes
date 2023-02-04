import sqlite3

conn = sqlite3.connect("job.db")

conn.execute('''CREATE TABLE IF NOT EXISTS Job(
    job_id VARCHAR(5) PRIMARY KEY NOT NULL,
    job_title TEXT NOT NULL,
    Min_salary INTEGER NOT NULL,
    Max_salary INTEGER NOT NULL
);
''')

conn.execute('''INSERT INTO Job(job_id, job_title, Min_salary, Max_salary)
      VALUES('AK56F','Real estate agent', 500000, 900000),
            ('HKJ67', 'Computer programmer', 7000000, 100000000),
            ('JH624', 'Teacher', 5000000, 20000000),
            ('IFR8', 'Veterinarian', 800000, 100000000),
            ('6478F', 'Accountant', 3000000, 200000000)
''')

query = 'SELECT * FROM Job;'
for i in conn.execute(query):
    print(i)
