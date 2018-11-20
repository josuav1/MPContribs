import os

DEBUG = True
JSON_ADD_STATUS = False
FLASK_LOG_LEVEL = 'DEBUG' if DEBUG else 'WARNING'
SECRET_KEY = b'super-secret' # reset in local prod config
API_CHECK_ENDPOINT = 'https://materialsproject.org/rest/api_check'
MONGODB_SETTINGS = {
    'host': "mongodb+srv://{0}/mpcontribs?retryWrites=true".format(
        os.environ.get('MPCONTRIBS_MONGO_HOST', 'localhost')
    ), 'connect': False
}
SWAGGER = {"specs": [
    {
        "endpoint": 'apispec',
        "route": '/apispec.json',
        "rule_filter": lambda rule: True,  # all in
        "model_filter": lambda tag: True,  # all in
    }
]}
TEMPLATE = {
    "swagger": "2.0",
    "info": {
        "title": "MPContribs API",
        "description": "Operations to retrieve materials data contributed to MP",
        "termsOfService": "http://me.com/terms",
        "version": None,
        "contact": {
            "name": "Materials Project",
            "email": "phuck@lbl.gov",
            "url": "https://materialsproject.org",
        },
        "license": {
            "name": "Apache 2.0",
            "url": "https://www.apache.org/licenses/LICENSE-2.0.html"
        }
    },
    "securityDefinitions": {
        "ApiKeyAuth": {
            'description': 'MP API key to authorize requests',
            'name': 'X-API-KEY',
            'in': 'header',
            'type': 'apiKey'
        }
    },
    "security": [{"ApiKeyAuth": []}]
    #"host": "mysite.com",  # overrides localhost:500
    #"basePath": "/api",  # base bash for blueprint registration
    #"schemes": [ "http", "https" ],
    #"operationId": "getmyData"
}
