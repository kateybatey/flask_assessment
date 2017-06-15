from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined


app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

@app.route("/")
def index():
    """Home page"""

    return render_template('index.html')

@app.route('/application-form', methods=["GET"])

def application_form():
	"""Displays a welcome message and link to application-form.html"""

    return render_template("application-form.html")

@app.route('/application-success', methods=["POST"])

def application():
	"""takes user input from form and returns their form input
	in application-response.html"""

    first_name = request.form.get("firstname")
    last_name = request.form.get("lastname")
    salary = request.form.get("salary")
    selection = request.form.get("selection")

    return render_template("application-response.html",
                            first_name=first_name, #feeding the user input into jinja
                            last_name=last_name,
                            salary=salary,
                            selection=selection)



if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
