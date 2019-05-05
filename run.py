# run.py
import os

from app import app

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)

os.popen("export FLASK_APP=run.py")
os.popen("flask run")
