
from django.http import HttpResponse
from django.shortcuts import render
from pymongo import MongoClient

# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

# mongo stuff.. 27020 is the port im running on
client = MongoClient('localhost', 27020)
db = client.bittopia
user_collection = db.user_collection

def index(request):
    if request.method == 'GET':
        return render(request, 'bittopia/index.html', {})
    elif request.method == 'POST':
        params = request.POST
        user = params["email"]
        password = params["password"]

        logger.info("log in attempt: by {0}".format(user))
        existing_user = user_collection.find_one({"email": email})

        if existing_user:
            if existing_user['password'] == password:
                logger.info("password doesn't match")
            else:
                logger.info("successful login")
                # redirect to main page

        user = { "email" : "mduppes@gmail.com",
                 "password": "what"
                 }
        user_collection.insert(
            user
    )


#return HttpResponse("Front page + login screen")

def signup(request):
    return HttpResponse('signup page')


