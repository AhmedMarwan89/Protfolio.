from flask import Flask , render_template , escape , redirect , request
import venv
import csv
#how to activate the virtual environment > venv\Scripts\activate.bat

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/<string>")
def hello_world2(string):
    return render_template(escape(string))





def save ( data):
    with open ( 'data_base.csv' ,newline='', mode= 'a') as dataBase :
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv.writer(dataBase, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL).writerow([email,subject ,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submitform():
    if request.method=='POST' :
        try :
            save(request.form.to_dict())
            return redirect('/thanks.html')
        except : 
            return 'the method is post but also there is some thing wrong '
    else : 
        return 'some thing is wrong'
    