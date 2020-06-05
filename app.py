from flask import Flask
from flask import render_template
app=Flask(__name__)

@app.route('/homepage')
def homepage():
     return render_template("/index.html")

@app.route('/login')
def login():
     return render_template("/login.html")


@app.route('/pages/Staffs/dashboardstaffs')
def staffdashboard():
    return render_template("/pages/Staffs/dashboardstaffs.html")

@app.route('/pages/Staffs/userprofilestaffs')
def userprofilestaffs():
    return render_template("/pages/Staffs/userprofilestaffs.html")


@app.route('/pages/Staffs/coursedocumentsstaffs')
def coursedocumentsstaffs():
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

@app.route('/pages/Admin/dashboardadmin')
def dashboardadmin():
    return render_template("/pages/Admin/dashboardadmin.html")



if __name__=='__main__':
    app.run(debug=True)