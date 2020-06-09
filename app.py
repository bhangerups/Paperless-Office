from flask import Flask
from flask import render_template,request,redirect,url_for
import os
from flask import flash
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import UserMixin
#from flask import win10toast

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///paperlessoffice.db'
app.config['SECRET_KEY']= 'arproject'

db=SQLAlchemy(app)
bcrypt=Bcrypt(app)

class registration(db.Model,UserMixin):
    id=db.Column(db.Integer, primary_key = True)
    fullname=db.Column(db.String(60), nullable=False)
    collegename=db.Column(db.String(100), nullable=False)
    username=db.Column(db.String(15), unique=True , nullable=False)
    password=db.Column(db.String(20),nullable=False)
    dob=db.Column(db.String(15) , nullable=False)
    contact_no=db.Column(db.Integer , nullable=False)
    address=db.Column(db.String(100), nullable=False)
    about_me=db.Column(db.String(300), nullable=False)
    user_type=db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"registration('{self.fullname}','{self.collegename}','{self.username}','{self.password}','{self.dob}','{self.contact_no}','{self.address}','{self.about_me}','{self.user_type}')"

@app.route('/homepage')
def homepage():
     return render_template("/index.html")

@app.route('/login',methods=['GET','POST'])
def login():
    print("In login")
    if request.method == 'POST':
        user_type = request.form.get('usertype')
        username = request.form.get('username')
        password = request.form.get('password')
        user = registration.query.filter_by(username=username).first()
        if user and user.password==password:
            if user.user_type=='Staff':
                return render_template("/pages/Staffs/dashboardstaffs.html")
            if user.user_type=='Higher_Authority':
                return render_template("/pages/HigherAuthority/dashboardhigher.html")
        return render_template("/login.html")


@app.route('/pages/Staffs/dashboardstaffs')
def staffdashboard():
    return render_template("/pages/Staffs/dashboardstaffs.html")

#user profile
@app.route('/pages/Staffs/userprofilestaffs',methods=['GET','POST'])
def userprofilestaffs():
    if request.method == 'POST':
        fullname= request.form.get('firstname')+' '+request.form.get('lastname')
        collegename= request.form.get('collegename')
        emailaddress= request.form.get('emailaddress')
        password=request.form.get('password')
        confirm_password=request.form.get('confirm_password')
        dob= request.form.get('dob')
        contact_no= request.form.get('contact')
        address= request.form.get('address')
        about_me=request.form.get('aboutme')
        print(fullname,collegename,emailaddress,dob,password,contact_no,address,about_me)
        data = registration(fullname=fullname,collegename='MGM',username=emailaddress,password=password,dob=dob,contact_no=contact_no,address=address,about_me=about_me,user_type="Staff")
        db.session.add(data)
        db.session.commit()
        return render_template("/pages/Staffs/userprofilestaffs.html")


#upload file
@app.route('/pages/Staffs/coursedocumentsstaffs', methods=['GET','POST'])
def coursedocumentsstaffs():
    if request.method == 'POST':
        print("in success")  
        f = request.files['uploadobjective']  
        f.save(os.path.join(app.root_path, 'Documents',f.filename))  
        print( os.path.join(app.root_path, 'Documents',f.filename))
    return render_template("/pages/Staffs/coursedocumentsstaffs.html")

@app.route('/pages/Staffs/syllabusdocumentsstaffs')
def syllabusdocumentsstaffs():
    return render_template("/pages/Staffs/syllabusdocumentsstaffs.html")

@app.route('/pages/Staffs/paperanalysis')
def paperanalysis():
    return render_template("/pages/Staffs/paperanalysis.html")

@app.route('/pages/Staffs/resultanalysisstaffs')
def resultanalysisstaffs():
    return render_template("/pages/Staffs/resultanalysisstaffs.html")

@app.route('/pages/Staffs/notificationsstaffs')
def notificationsstaffs():
    return render_template("/pages/Staffs/notificationsstaffs.html")


@app.route('/pages/HigherAuthority/dashboardhigher')
def dashboardhigher():
    return render_template("/pages/HigherAuthority/dashboardhigher.html")

@app.route('/pages/HigherAuthority/validaterequesthigher')
def validaterequesthigher():
    return render_template("/pages/HigherAuthority/validaterequesthigher.html")

@app.route('/pages/HigherAuthority/approvedrequesthigher')
def approvedrequesthigher():
    return render_template('/pages/HigherAuthority/approvedrequesthigher.html')

@app.route('/pages/Admin/dashboardadmin')
def dashboardadmin():
    return render_template("/pages/Admin/dashboardadmin.html")

# higher authority profile
@app.route('/pages/HigherAuthority/profilehigherauthority',methods=['GET','POST'])
def profilehigherauthority():
    if request.method == 'POST':
        fullname= request.form.get('firstname')+' '+request.form.get('lastname')
        collegename= request.form.get('collegename')
        emailaddress= request.form.get('emailaddress')
        password=request.form.get('password')
        confirm_password=request.form.get('confirm_password')
        dob= request.form.get('dob')
        contact_no= request.form.get('contact')
        address= request.form.get('address')
        about_me=request.form.get('aboutme')
        print(fullname,collegename,emailaddress,dob,password,contact_no,address,about_me)
        data = registration(fullname=fullname,collegename='MGM',username=emailaddress,password=password,dob=dob,contact_no=contact_no,address=address,about_me=about_me,user_type="Higher_Authority")
        db.session.add(data)
        db.session.commit()
    return render_template("/pages/HigherAuthority/profilehigherauthority.html")

@app.route('/')  
def upload():  
    return render_template("/pages/Staffs/coursedocumentsstaffs.html")  
 
@app.route('/success', methods = ['POST'])  
def success():  
    print("In body")
    if request.method == 'POST':
        print("in success")  
        f = request.files['uploadobjective']  
        f.save(os.path.join(app.root_path, 'Documents',f.filename))  
        print( os.path.join(app.root_path, 'Documents',f.filename))
        return render_template("/pages/Staffs/success.html",name=f.filename)



if __name__=='__main__':
    app.run(debug=True)