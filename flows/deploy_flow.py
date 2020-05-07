import prefect_deployment
import demo_flow


prefect_deployment.deploy.deploy_flow(
    demo_flow.flow,
    requirements=[],  # requirements="./requirements.txt",
    run=False
)
