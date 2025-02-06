from flask import Blueprint, jsonify, current_app

main_bp = Blueprint("main", __name__)

@main_bp.route("/", methods=["GET"])
def home():
    print(current_app.config["SPREADSHEET_ID"])
    spreadsheet_id = current_app.config["SPREADSHEET_ID"]
    day = current_app.sheets_service.get_day("\'meso 1\'", 0, 0)
    return jsonify({"message": day})

@main_bp.route("/meso/<week>", methods=["GET"])
def week(week):
    response = current_app.sheets_service.get_week("\'meso 1\'", int(week))
    return jsonify({"message": response})

@main_bp.route("/meso/<week>/<day>", methods=["GET"])
def day(week, day):
    response = current_app.sheets_service.get_day("\'meso 1\'", int(week), int(day))
    return jsonify({"message": response})