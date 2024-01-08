from flask import Flask, jsonify, request

app = Flask(__name__)

"""
Fetch top track from artist on Spotify
    Returns:
        json: { top_track: [arist_name, top_track, link]}
"""


@app.route("/track")
def get_top_track():
    # Get input from params
    # Call Spotify client to get artist top track
    # Return object with info
    return []
