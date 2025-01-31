from flask import Blueprint, jsonify, current_app

main_bp = Blueprint("main", __name__)

@main_bp.route("/", methods=["GET"])
def home():
    print(current_app.config["SPREADSHEET_ID"])
    spreadsheet_id = current_app.config["SPREADSHEET_ID"]
    return jsonify({"message": spreadsheet_id})
