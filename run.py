#!flask/bin/python

from app import app
app.run(port=int("80"), debug=True)
