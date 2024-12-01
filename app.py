from flask import Flask, render_template, request, redirect, url_for
import pg8000

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        level = request.form["level"]
        # Redirect to the timetable page, passing the level as a query parameter
        return redirect(url_for("timetable", level=level))
    
    return render_template("index.html")

@app.route("/timetable", methods=["GET"])
def timetable():
    level = request.args.get("level")  # Get level from query parameter
    if not level:
        return "Level not provided", 400

    # Connect to PostgreSQL database
    conn = pg8000.connect(
        user="postgres", 
        password="postgres", 
        host="rakhmatilla.ct4a02uyqid9.us-east-1.rds.amazonaws.com", 
        port=5432, 
        database="rakhmatilla"
    )

    cur = conn.cursor()
    query = "SELECT * FROM timetable WHERE level = %s"
    cur.execute(query, (level,))
    rows = cur.fetchall()

    # Pass the fetched rows to the template
    if rows:
        return render_template("timetable.html", level=level, data=rows, message="")
    else:
        return render_template("timetable.html", level=level, data=[], message="No data found for this level.")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
