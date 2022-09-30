from flask import Flask ,jsonify
import requests
import json




app= Flask(__name__)

BASE_URL ="https://mobipolar.online/api/property/lagecy_v1?bracket_key={}"

@app.route('/')
def index():
  return "<h1>P</h1>"


def loadfromFile(file_name):
 try:
  f = open('jsonbackend/'+file_name)
  data = json.load(f)
  return data
 except Exception as e:
    return None


@app.route('/<path>',methods=['GET'])
def getSettigns(path):
    db_data = requests.get(BASE_URL.format(path))
    try :
     return db_data.json()["data"]
    except Exception as e :
     resp = loadfromFile(path)   
     if(resp==None):
        return resp
     else :
      return loadfromFile(path)
        
        
if __name__ == "__main__":
    app.run(host="0.0.0.0",threaded=True)




