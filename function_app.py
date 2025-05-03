import azure.functions as func
import json

# Initialize a global counter (in-memory, will reset on function app restart)
visit_count = 0

def main(req: func.HttpRequest) -> func.HttpResponse:
    global visit_count

    logging.info('Python HTTP trigger function processed a request.')

    # Increment the visit count
    visit_count += 1

    # Return the visit count as JSON
    return func.HttpResponse(
        json.dumps({"count": visit_count}),
        mimetype="application/json",
        status_code=200
    )