from flask import Flask, redirect, render_template, request, url_for, jsonify
from tabulate import tabulate

from api import ScoredStory

app = Flask(__name__)


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        story = request.form["story"]
        score_types = ['general_consistency_score', 'character_consistency_score', 'plot_consistency_score']
        scored_story = ScoredStory(story)
        scored_story.calculate_score(score_types)

        # Create a list of tuples containing the field names and their values
        table_data = [
            ("General Consistency Score", scored_story.score.general_consistency_score),
            ("Character Consistency Score", scored_story.score.character_consistency_score),
            ("Plot Consistency Score", scored_story.score.plot_consistency_score)
        ]

        # Generate the table using tabulate and convert it to HTML string
        table_html = tabulate(table_data, headers=["Field", "Value"], tablefmt="html")
        print(table_html)

        return render_template("index.html", table=table_html)

    result = request.args.get("result")
    return render_template("index.html", result=result)

