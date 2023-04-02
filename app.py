from flask import Flask ,jsonify
import requests
import logging
import json




app= Flask(__name__)
logging.basicConfig(filename='app.log', format='%(asctime)s: %(levelname)s, %(message)s', level=logging.DEBUG)
BASE_URL ="https://mobipolar.online/api/property/lagecy_v1?bracket_key={}"

@app.route('/')
def index():
  return "<h1>P</h1>"



def readJSONfile(path):
  try :
   with open('miragetanger/jsonbackend/'+path, 'r') as file:
        content = json.load(file)
   return content
  except Exception as e:
    print(e)
    return None  
  
@app.route('/<path>',methods=['GET'])
def getapp(path):
   data = requests.get(BASE_URL.format(path))
   try :
    if(data.json()['code']==404):
     try :
       resp = readJSONfile(path)
       if(resp==None):
        return jsonify({"message":"not found"}) 
       else :
        return readJSONfile(path)
     except Exception as e:
       logging.error(e)
       return jsonify({"message":str(e)}) 
    else :
     return data.json()
   except Exception as e:
     print(e) 

if __name__ == "__main__":
    app.run(host="0.0.0.0",threaded=True)



