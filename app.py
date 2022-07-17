#from crypt import methods
from flask import Flask,request,jsonify,render_template
app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def Hello():
    return "Hello World"

if __name__=='__main__':
    app.run(debug=True)
