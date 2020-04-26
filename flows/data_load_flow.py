import prefect
#import prefect.context
from prefect import task, Flow, Parameter
from prefect.environments.storage import Docker
import os
import subprocess
import sys
import pandas as pd
import cloudpickle
import functools

#import sys
#sys.path.append("C:/Users/dfleetwood/Documents/prefect_deployment")

#import prefect_deployment

# def flow_email_state_handler(obj, old_state, new_state):
#     # print(new_state)
#     # try:

#     tasks = obj.tasks  # prefect.context.to_dict() #.get("date")
#     for task in tasks:
#         if isinstance(task, Parameter) & (task.name == 'email_address'):
#            print ("Found it ")
#            email_address = task
#     try:
#         email_address  =  str (email_address.run())
#     except Exception as e:
#         print (e)
        

    # get(
    #     # "parameters", {}).get("to_email_address")
    #     print("Params")
    #     print(email_address)
    #     if email_address is not None:
    #         print("Email address: " + str(email_address))
    #         send_email(email_address, "Prefect flow: " +
    #                    str(obj.name), str(new_state))
    #         print("Sent email")
    #     else:
    #         print("None email adrress")
    # except Exception as e:
    #     print(e)

    #return new_state


# @task
# def setup(email_address):
#     prefect.context['email_address'] = email_address


@task(name="Data check load", log_stdout=True)
def data_check():
    # to_email_address = prefect.context.to_dict()#  parameters #prefect.context.get("parameters", {})  # .get("to_email_address")
    # print("Params: ")  # + to_email_address)
    # print(type (to_email_address))
    # print(str (to_email_address))
    # p = prefect.context.get("parameters", {})#.get("to_email_address")
    # print ("Flow name" + str (p))  #str (prefect.context.parameters))

    logger = prefect.utilities.logging.get_logger()

    with open("./data/data_file.csv") as f:
        data_x = pd.read_csv(f)
    logger.debug("Loaded data")
    logger.debug(data_x.shape)
    print(data_x.shape)
    # print(param_t)

# @task(name="Data check v2 dot", log_stdout=True)
# def data_check_v2():

#     logger = prefect.utilities.logging.get_logger()

#     with open ("../data/raw/sysomos_heam_tweet_sample/sysomos_heam_tweet_sample-050320-1531.csv") as f:
#         data_x = pd.read_csv (f)
#     logger.debug ("Loaded data")
#     logger.debug (data_x.shape)


with Flow("data_load_test") as flow:
    #test_param = Parameter("test_param", default="a")
    flow.add_task(data_check)

    # flow.add_task(data_check)
    #flow.add_task(Parameter("test_param", default="a"))

    #flow = Flow("data_load_test",  tasks=[data_check])

    # with open("./data_load_test", "wb") as f:
    #     cloudpickle.dump(flow, f)
    #flow.save ("./data_load_test")
 #   flow.add_task(Parameter("email_address",
 #                             default="darrenfleetwood@gmail.com"))
    #data_check.set_upstream(setup(email_address))

    #flow.add_task(Parameter("to_email_address", to_email_address))
    #environment_setup.set_upstream(task, flow=flow)

    # flow.state_handlers.append(flow_email_state_handler)
#flow.state_handlers.append(functools.partial (prefect_deployment.deploy.flow_email_state_handler, email_address = email_address))
#flow.state_handlers.append(prefect_deployment.deploy.flow_email_state_handler)

#flow.run()
