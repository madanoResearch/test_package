import prefect_deployment
import data_load_flow

import os

if __name__ == '__main__':

    dir_path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(dir_path)
    print(dir_path)

    with open("../requirements.txt") as f:
        requirements = f.readlines()

    prefect_deployment.deploy.deploy_flow(
        data_load_flow.flow,
        api_host="104.47.157.14",
        requirements=requirements,
        project="test-project",
        synch_dvc=True,
        run=True,
        # to_email_address="darren.fleetwood@madano.com",
        working_dir=dir_path
    )
