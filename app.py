from datetime import datetime
from flask import Flask, render_template, request,redirect
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

'''
we are creating db for our website once you've written the above commands,
go to terminal and type "python"
then write "app.create_all()"
'''


class Todo(db.Model):
    sno = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(200),nullable=False)
    desc = db.Column(db.String(500),nullable=False)
    date_created = db.Column(db.DateTime,default = datetime.utcnow) #to adding a time stap in db

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"



 

@app.route('/', methods=['GET','POST'])   #decorator  
def home(): 
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        todo =Todo(title = title, desc = desc )
        db.session.add(todo)
        db.session.commit()
    alltodo =Todo.query.all()
    return render_template('index.html',alltodo=alltodo)


@app.route('/delete/<int:sno>')   #decorator  
def delete(sno):
    todo = Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")


@app.route('/update/<int:sno>', methods=['GET','POST'])   #mai chata hun ki jb koi /update/sno mile tbb ye pass ho jae or update function me ghus jae
def update(sno):
    if request.method=='POST':
        title = request.form['title']
        desc = request.form['desc']
        todo = Todo.query.filter_by(sno=sno).first()
        todo.title = title
        todo.desc = desc
        db.session.add(todo)
        db.session.commit()
        return redirect("/")

    todo = Todo.query.filter_by(sno=sno).first()    
    return render_template('update.html', todo =todo)


@app.route('/show')   #decorator  
def products():
    alltodo = Todo.query.all()
    print(alltodo)
    return '<h1>Hello world</h1>'

if __name__ =="__main__":
    app.run(debug=True,port=8000)