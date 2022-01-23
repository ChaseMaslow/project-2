"""
John Doe's Flask API.
"""

from flask import Flask, redirect, url_for, abort, send_from_directory
import os
import config

docroot = "./pages"
docs = os.listdir(docroot)

app = Flask(__name__)

@app.route("/")
def hello():
    return "<p>Hello!</p>"

@app.route("/<page>")
def serve(page):
    if "~" in page or ".." in page:
        abort(403)
    return send_from_directory(docroot, page), 200

@app.errorhandler(404)
def page_not_found(error):
    return send_from_directory(docroot, "404.html"), 404

@app.errorhandler(403)
def access_forbidden(error):
    return send_from_directory(docroot, "403.html"), 403

if __name__ == "__main__":
    launch = config.configure()
    app.run(debug = launch['SERVER']['DEBUG'], host='0.0.0.0', port = launch['SERVER']['PORT'])
