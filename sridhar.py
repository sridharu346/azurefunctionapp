## Function App to deploy in Azure for testing purposes.
import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.function_name(name="functiontesting")
@app.route(route="functiontesting")
def functiontesting(req: func.HttpRequest) -> func.HttpResponse:
    """
    HTTP-triggered Azure Function that greets the user and returns the sum of a + b.
    """
    logging.info('Python HTTP trigger function processed a request.')

    a = 2
    b = 3
    c = a + b

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            req_body = None
        if req_body:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(
            f"Hello, {name}. This HTTP triggered function executed successfully. The sum of a + b is {c}"
        )
    else:
        return func.HttpResponse(
            f"This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response. The sum of a + b is {c}",
            status_code=200
        )