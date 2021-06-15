from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///posts.db'
db=SQLAlchemy(app)

class store(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(20))
    Year_of_joining=db.Column(db.Integer)
    City=db.Column(db.String(15))
    
@app.route('/')
def upload():
    return render_template('post.html')
    

@app.route('/upload',methods=['POST'])
def loadtodb():
    file=request.files['inputfile']
    file_csv=open(file)
    file_csv_read=csv.reader(file_csv,delimiter=',')
    for row in file_csv_read:
        obj=store(id=row[0],name=row[1],Year_of_joining=row[2],City=row[3])
        db.session.add(obj)
        db.session.commit()
    return redirect('/')

    
   

if __name__=="__main__":
    app.run(debug=True)

