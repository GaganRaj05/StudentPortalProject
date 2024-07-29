from flask import Flask,render_template,flash,redirect,url_for,session
from forms import loginForm,queryForm
from flask_mysqldb import MySQL

#
app = Flask(__name__)
mysql=MySQL(app)
app.config["SECRET_KEY"]="45788899"
app.config["MYSQL_DB"]="studentportal"
app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]="Wanderer89"


@app.route("/",methods=["GET","POST"])
def login():
    form=loginForm()
    session['user_id']=None
    session['Fname']=None
    session['Lname']=None
    if form.validate_on_submit():
        cursor=mysql.connection.cursor()
        username=form.username.data
        password=form.password.data
        cursor.execute("select id,F_name,L_name, Password from STUDENT where id=%s and Password=%s",(username,password))
        student = cursor.fetchone()
        if student is None:
            cursor.execute("select id,password from Admin where id=%s and Password=%s",(username,password))
            admin = cursor.fetchone()
            if admin:
                session['user_id']=admin[0]
                flash(f"Log In successfull","success")
                return redirect(url_for('admin'))
            else:
                flash(f"Invalid username or Password Entered ")
                return redirect(url_for('login'))
        else:
            session['user_id']=student[0]
            session['Fname']=student[1]
            session['Lname']=student[2]
            flash(f"Log In successfull","success")
            return redirect(url_for('home'))
    return render_template("login.html",form=form)

