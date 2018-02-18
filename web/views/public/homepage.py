from flask import render_template

from . import blueprint


@blueprint.route("/", methods=["GET"])
def homepage():
    return render_template(
        "public/homepage.html"
    )
