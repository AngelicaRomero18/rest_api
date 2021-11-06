from flask import Flask, jsonify

app = Flask(__name__)

import controllers.casesController as controller

@app.route("/api/cases")
def getCasesApi():
    cases = controller.get_cases()
    return jsonify(cases)


if __name__ == '__main__':
    app.run(debug=True, port=5000)