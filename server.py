from re import A
from flask import Flask, request
from MarkdownParser import *
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"


@app.route("/parseMarkdown", methods=["POST"])
def parse_markdown():
    if request.method == "POST":

        file = request.files["file"]
        file.save(os.path.join("", "input.txt"))
        markdownParser = MarkdownParser("input.txt")
        return markdownParser.parseMarkdown()
