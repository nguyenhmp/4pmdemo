from myconnection import MySQLConnector
from flask import Flask, render_template, request, redirect
app = Flask(__name__)
app.secret_key = "helrakjdl;kfsadfs"
mysql = MySQLConnector(app, "airbnbdb")

@app.route("/")
def index():
	x = mysql.query_db("SELECT * FROM users")
	return render_template("users.html", all_users=x)
	# # print x
	# for user in x:
	# 	print user
	# 	print user["id"]
	# 	print user["email"]
	# 	print user["password"]
	# 	print user["created_at"]
	# 	print user["updated_at"]



@app.route("/add", methods=["POST"])
def add():
	query = "INSERT INTO users (`email`, `password`, `created_at`, `updated_at`) VALUES (:spot_one, :spot_two, now(), now());"
	data = {
		'spot_one':  request.form['email'],   
		'spot_two':  request.form['password'],
	}
	mysql.query_db(query, data)

# //querry to insetd da
	return redirect("/")

@app.route("/create")
def create():
	return render_template("create.html")

app.run(debug=True)
