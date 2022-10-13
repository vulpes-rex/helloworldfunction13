import logging

import azure.functions as func
import pymongo
import os
import json
from bson.json_util import dumps

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    request = req.get_json()
    if request:
        try:
            # add your connection string here
            url = os.environ["MyDbConnection"]
            client = pymongo.MongoClient(url)
            # you will need this fill in
            database = client['test'] # Change the MongoDB name
            collection = database['notes']    # Change the collection name
            # replace the insert_one variable with what you think should be in the bracket
            collection.insert_one(request)
            # we are returnign the request body so you can take a look at the results
            return func.HttpResponse(req.get_body())
        except ValueError:
            return func.HttpResponse('Database connection error.', status_code=500)
    else:
        return func.HttpResponse(
            "Please pass the correct JSON format in the body of the request object",
            status_code=400
        )