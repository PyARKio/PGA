# -- coding: utf-8 --
from __future__ import unicode_literals
import bottle
import pymongo
import sys


connection = pymongo.MongoClient("mongodb://localhost")
db = connection.test


@bottle.route('/hello/<name>')
def index_too(name):
    return name


@bottle.route('/')
def index():
    users = db.users.find()
    return bottle.template('index', {"users": users})


@bottle.post('/submit')
def submit_page():
    user = {'name': bottle.request.forms.get("name"), 'age': bottle.request.forms.get("age")}
    db.users.insert(user)
    bottle.redirect('/')


bottle.debug()
bottle.run(host="localhost", port=8080)
