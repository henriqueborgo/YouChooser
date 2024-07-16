#API to interact with data files/database
#Update files/database content
#URL base - localhost
#API endpoints
""" 
Modify JSON file - localhost/dataJSON (PUT)
Input data in Permanent Database- localhost/dataPermanent (POST)
Delete Temporary database- localhost/dataTemporary (DELETE) """

#import libraries
from flask import Flask, jsonify, request
from flask_cors import CORS
import json


app = Flask(__name__)
CORS(app)

#Input answer to JSON file
@app.route('/dataJSON/<int:answer>', methods=['PUT'])
def answerUserLiked(answer):
    try:
        #opens the JSON file in read mode
        with open('videoInformation.json', 'r') as jsonFile:
            jsonData = json.load(jsonFile)
        #input the data into the object
        jsonData['answerUser'] = answer
        #opens the JSON file in write mode and overide the data
        with open('videoInformation.json', 'w') as jsonFile:
            json.dump(jsonData, jsonFile, indent=4)
        return jsonify({'message': 'Answer updated successfully'}), 200
    except Exception as e:
            return jsonify({'error': str(e)}), 500

if __name__=='__main__':
    app.run(port=5000, host='localhost', debug=True)