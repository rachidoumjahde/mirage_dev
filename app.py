from flask import Flask
import requests
import logging
import json



app= Flask(__name__)
logging.basicConfig(filename='app.log', format='%(asctime)s: %(levelname)s, %(message)s', level=logging.DEBUG)
BASE_URL ="https://mobipolar.online/api/property/lagecy_v1?bracket_key={}"

@app.route('/')
def index():
  return "<h1>P</h1>"


# def readJSONfile(path):
#   try :
#    f = open("jsonbackend/"+path)
#    data = json.load(f)
#    return data
#   except Exception as e:
#     return None  

# @app.route('/<path>',methods=['GET'])
# def getapp(path):
#   try :
#    data = requests.get(BASE_URL.format(path))
#    return data.json()["data"]
#   except Exception as e  :
#     logging.error(e)
#     try :
#       resp = readJSONfile(path)
#       if(resp==None):
#        return jsonify({"message":"not found"}) 
#       else :
#        return readJSONfile(path)
#     except Exception as e:
#       logging.error(e)
#       return jsonify({"message":str(e)}) 

if __name__ == "__main__":
    app.run(host="0.0.0.0",threaded=True)




