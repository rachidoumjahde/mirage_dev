from flask import Flask ,jsonify




app= Flask(__name__)

BASE_URL ="https://mobipolar.online/api/property/lagecy_v1?bracket_key={}"

@app.route('/')
def index():
  return "<h1>P</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0",threaded=True)




