import os
import data_load_flow
import sys


sys.path.append('C:/Users/dfleetwood/Documents/prefect_deployment')

import prefect_deployment


# if __name__ == '__main__':

# dir_path = os.path.dirname(os.path.realpath(__file__))
# os.chdir(dir_path)
# print(dir_path)

# with open("../requirements.txt") as f:
#    requirements = f.readlines()

# XYZ
prefect_deployment.deploy.deploy_flow(
    data_load_flow.flow,
    # api_host="104.47.157.14",
    requirements="./requirements.txt",
    # project="test-project",
    # synch_dvc=True,
    run=True,
    email_address="darrenfleetwood@gmail.com"
    # working_dir=dir_path
)
