from flask import Flask
from flask import render_template
app=Flask(__name__)

@app.route('/pages/Staffs/dashboardstaffs')
def staffdashboard():
    return render_template("/pages/Staffs/dashboardstaffs.html")

@app.route('/pages/HigherAuthority/dashboardhigher')
def dashboardhigher():
    return render_template("/pages/HigherAuthority/dashboardhigher.html")

@app.route('/pages/Admin/dashboardadmin')
def dashboardadmin():
    return render_template("/pages/Admin/dashboardadmin.html")



if __name__=='__main__':
    app.run(debug=True)