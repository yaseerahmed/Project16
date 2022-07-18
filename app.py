#from crypt import methods
from flask import Flask,request,jsonify,render_template
from housing.logger import logging
from housing.exception import HousingException
import sys
app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def Hello():
    try:
        raise Exception("we are testing exception")
    except Exception as e:
        housing = HousingException(e,sys)
        logging.info(housing.error_message)
    logging.info("we are testing logs")
    return "Hello World"

if __name__=='__main__':
    app.run(debug=True)
