from myconnection import MySQLConnector
from flask import Flask, render_template
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

app.run(debug=True)
