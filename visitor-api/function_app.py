import logging
import azure.functions as func
import os
from azure.data.tables import TableServiceClient, TableEntity
import json

app = func.FunctionApp()

@app.function_name(name="visitorcounter")
@app.route(route="visitorcounter", auth_level=func.AuthLevel.ANONYMOUS)
def visitorcounter(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Function visitorcounter triggered")

    try:
        conn_str = os.getenv("AzureWebJobsStorage")
        if not conn_str:
            logging.error("AzureWebJobsStorage is missing")
            return func.HttpResponse("Missing config", status_code=500)

        table_client = TableServiceClient.from_connection_string(conn_str).get_table_client("VisitorCounter")

        try:
            entity = table_client.get_entity(partition_key="counter", row_key="1")
            entity["count"] += 1
            table_client.update_entity(mode="replace", entity=entity)
        except Exception as e:
            logging.warning(f"Entity not found. Creating new one. Error: {e}")
            entity = TableEntity()
            entity["PartitionKey"] = "counter"
            entity["RowKey"] = "1"
            entity["count"] = 1
            table_client.create_entity(entity)

        return func.HttpResponse(
            body=json.dumps({"count": entity["count"]}),
            mimetype="application/json",
            status_code=200
        )

    except Exception as e:
        logging.error(f"Unhandled exception: {e}", exc_info=True)
        return func.HttpResponse("Server Error", status_code=500)
