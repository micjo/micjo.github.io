from flask import Flask, render_template, request, app, redirect, url_for
from flask_frozen import Freezer

app = Flask(__name__)
app.config["FREEZER_DESTINATION"] = "docs"

posts = {
        "std_error_code" : {
            "title": "Plugging std error code",
            "description": "Extending std error_code to contain custom error codes",
            "date": "2021 05 08",
            "tags" : ["c++","error handling", "standard library"]
        },
        "sem_mutex" : {
            "title": "Semaphore and Mutex",
            "description": "The differences between a semaphore and a mutex",
            "date": "2018 02 17",
            "tags" : ["multithreading","mutex","semaphore"]
            },
        "fosdem_2018_gstreamer" : {
            "title": "Gstreamer",
            "description": "GStreamer related fosdem talks",
            "date": "2018 02 11",
            "tags" : ["fosdem 2018","gstreamer","FOSS"]
        },
        "fosdem_2018" : {
            "title": "Fosdem 2018",
            "description": "Fosdem 2018",
            "date": "2018 02 11",
            "tags" : ["fosdem 2018","FOSS"]
        }
        }

@app.route("/index.html")
def dashboard():
    return render_template("home.html", posts=posts)

@app.route("/<postId>.html")
def post(postId):
    post_settings = posts[postId]
    html_page = postId + ".html"
    return render_template(html_page, post_settings=post_settings)

freezer = Freezer(app)
@freezer.register_generator
def post():
    for key in posts:
        yield {'postId': key}

freezer.freeze()
