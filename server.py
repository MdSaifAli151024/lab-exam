from flask import Flask


app = Flask(__name__)

courses = ['FCN',
           ' COSA',
            'SECURITY CONCEPTS',
            'ITIM & DEVOPS',
            'NDC',
            'PKI',
            'CYBER FORENSICS',
           ' COMPLIANCE AUDIT', 
           ' APPTITUDE and EFFECTIVE COMMUNICATION' ]


naam = [ 'Name : Md Saif Ali' , 'Course : PG-DITISS', ' PRN : 230344223027', 'PHONE NUMBER : 9934141981']


@app.route("/", methods=["GET"])
def root():
    return "<h1>welcome to ITIL EXAM</h1>"

@app.route("/modules", methods=["GET"])
def get_list():
    return courses

@app.route("/me", methods=["GET"])
def name():
    return naam



app.run(host="0.0.0.0", port=4000, debug=True)
