from prefect import task, Flow, Parameter
#import pandas as pd


@task
def hello():
    print("1")
    # return ("hello")


@task
def hello_again():
    print("2")


@task
def hello2():
    return ("hello2")


@task
def hello_again2(message):
    print(message)


# @task
# def task_with_retries():
#     print("hello")

# @task()  # (name="Data check load", log_stdout=True)
# def load_data():
#     with open("./data/data_file.csv") as f:
#         data = pd.read_csv(f)
#     return (data(data))


with Flow("demo_flow") as flow:

    hello_again.set_downstream(hello)

    message2 = hello2()
    hello_again2(message2)
    # flow.add_task(hello)

# flow.run()
