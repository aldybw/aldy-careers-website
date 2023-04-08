from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Jakarta, Indonesia',
    'salary': 'Rp. 7.000.000'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Bandung, Indonesia',
    'salary': 'Rp. 9.000.000'
  },
  {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Remote',
    # 'salary': 'Rp. 6.000.000'
  },
  {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'San Fransisco, USA',
    'salary': 'Rp. 8.000.000'
  },
]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name='Aldy')


@app.route("/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
