import prefect
from prefect import task, Flow, Parameter
from prefect.environments.storage import Docker
import os
import subprocess
import sys
import pandas as pd
import cloudpickle


@task(name="Data check load", log_stdout=True)
def data_check(param_t):

    logger = prefect.utilities.logging.get_logger()

    with open("./data/data_file.csv") as f:
        data_x = pd.read_csv(f)
    logger.debug("Loaded data")
    logger.debug(data_x.shape)
    print(data_x.shape)
    print(param_t)

# @task(name="Data check v2 dot", log_stdout=True)
# def data_check_v2():

#     logger = prefect.utilities.logging.get_logger()

#     with open ("../data/raw/sysomos_heam_tweet_sample/sysomos_heam_tweet_sample-050320-1531.csv") as f:
#         data_x = pd.read_csv (f)
#     logger.debug ("Loaded data")
#     logger.debug (data_x.shape)


with Flow("data_load_test") as flow:
    test_param = Parameter("test_param", default="a")
    data_check(test_param)

    # flow.add_task(data_check)
    #flow.add_task(Parameter("test_param", default="a"))

#flow = Flow("data_load_test",  tasks=[data_check])

# with open("./data_load_test", "wb") as f:
#     cloudpickle.dump(flow, f)
#flow.save ("./data_load_test")

# flow.run()
