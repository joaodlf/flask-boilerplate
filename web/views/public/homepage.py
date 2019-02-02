from flask import render_template

from web.views.blueprints import public_blueprint


@public_blueprint.route("/", methods=["GET"])
def homepage():
    return render_template(
        "public/homepage.html"
    )
