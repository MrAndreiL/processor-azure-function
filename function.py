import logging
import azure.functions as func

app = func.FunctionApp()

part1 = "Endpoint=sb://emailspam.servicebus.windows.net/;SharedAccess"
part2 = "KeyName=RootManageSharedAccessKey;SharedAccessKey=mvfrWyMCwI+kAN"
part3 = "MMKe9eQhaC/47foWkC4+ASbMInOqE="

NAMESPACE_CONNECTION_STRING = part1 + part2 + part3

@app.function_name(name="ServiceBusQueueTrigger1")
@app.service_bus_queue_trigger(arg_name="msg", 
                               queue_name="bprocessing", 
                               connection=NAMESPACE_CONNECTION_STRING)
def test_function(msg: func.ServiceBusMessage):
    logging.info('Python ServiceBus queue trigger processed message: %s',
                 msg.get_body().decode('utf-8'))
