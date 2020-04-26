import os
import data_load_flow
import sys


sys.path.append('C:/Users/dfleetwood/Documents/prefect_deployment')

import prefect_deployment


prefect_deployment.deploy.deploy_flow(
    data_load_flow.flow,
    requirements="./requirements.txt",
    run=True
    # email_address="darrenfleetwood@gmail.com"
)
