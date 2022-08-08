from flask import Blueprint, jsonify


api = Blueprint("api",__name__)


@api.route("/blogs/")
def blog_list():
    return jsonify([
        {
            "name":"anies", 
            "position":20,
        },
        {
            "name":"John", 
            "position":40,
        },
        {
            "name":"Philip", 
            "position":50,
        },
    ])


@api.get("/blogs/<int:id>")
def blog_retrieve(id):
    return "blog with id "+str(id)