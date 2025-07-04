import azure.functions as func
from azure.functions import HttpRequest
import logging

app = func.FunctionApp()

@app.function_name(name="HttpExample")
@app.route(route="HttpExample", auth_level="anonymous")
def http_example(req: HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            req_body = {}
        name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}!")
    else:
        return func.HttpResponse(
             "Please pass a name on the query string or in the request body",
             status_code=400
        )