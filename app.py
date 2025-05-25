from flask import Flask, request, jsonify
from rapidfuzz import process, fuzz
import pandas as pd

app = Flask(__name__)

# Load name list
df = pd.read_csv("name_dataset.csv")
names = df["Name"].tolist()

# Route for fuzzy matching
@app.route("/match", methods=["POST"])
def match_name():
    data = request.get_json()
    query = data.get("name", "")
    results = process.extract(query, names, scorer=fuzz.WRatio, limit=5)
    matches = [{"name": name, "score": score} for name, score, _ in results]
    return jsonify(matches)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
