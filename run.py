from app import app
from app.db import dbManager


if __name__ == "__main__":
    dbUtils = dbManager.DBConnection()
    dbUtils.create_tables()
    app.run(debug=True)