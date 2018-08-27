from app import app
from app.db import dbManager
from flask import jsonify

@app.errorhandler(405)
def url_not_found(error):
    return jsonify({'message': "Requested URL is invalid"}),405

@app.errorhandler(404)
def content_not_found(error):
    return jsonify({'message': "Requested url is not found"}),404

@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({'message': "Internal server error"}),500

if __name__ == "__main__":
    dbUtils = dbManager.DBConnection()
    dbUtils.create_tables()
    app.run(debug=True)