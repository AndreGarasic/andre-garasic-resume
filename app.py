from flask import Flask, render_template, jsonify

app = Flask(__name__)

EXPERIENCE = [
  {
    'id' : 1,
    'title' : 'Software engineer intern',
    'company' : 'Ericsson Nikola Tesla d.d.',
    'location' : 'Zagreb, Croatia'
  },
    {
    'id' : 2,
    'title' : 'Software developer',
    'company' : 'Ericsson Nikola Tesla d.d.',
    'location' : 'Zagreb, Croatia'
  }
]

@app.route("/")
def start():
  return render_template('home.html', 
                         experience=EXPERIENCE)

@app.route("/api/experience")
def list_experiences():
  return jsonify(EXPERIENCE)
  
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
