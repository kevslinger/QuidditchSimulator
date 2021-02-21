import numpy as np
import constants
import utils
from flask import Flask, render_template, request
import utils, constants
import season

app = Flask(__name__)


# Home page
@app.route("/")
def landing():
    LEAGUE_TABLE = utils.create_teams()
    print(LEAGUE_TABLE)
    LEAGUE_TABLE = season.simulate_season(LEAGUE_TABLE)
    return render_template("index.html", league_table=LEAGUE_TABLE, wins=constants.WINS, losses=constants.LOSSES, points_for=constants.POINTS_FOR,
    points_against=constants.POINTS_AGAINST, snitches_caught=constants.SNITCHES_CAUGHT,
    chaser=constants.CHASER, beater=constants.BEATER, keeper=constants.KEEPER,
    seeker=constants.SEEKER)

# Simulate Season
@app.route("/Simulate", methods=["POST"])
def simulate():
    if request.method == 'POST':
        print(LEAGUE_TABLE)
        return render_template("index.html", league_table=LEAGUE_TABLE, wins=constants.WINS, losses=constants.LOSSES, points_for=constants.POINTS_FOR,
    points_against=constants.POINTS_AGAINST, snitches_caught=constants.SNITCHES_CAUGHT,
    chaser=constants.CHASER, beater=constants.BEATER, keeper=constants.BEATER,
    seeker=constants.SEEKER)

if __name__ == '__main__':
    app.run(debug=True)