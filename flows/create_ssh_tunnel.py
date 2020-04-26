from sshtunnel import SSHTunnelForwarder
import sshtunnel
import getpass
import webbrowser


REMOTE_SERVER_IP = "104.47.157.14"
PRIVATE_SERVER_IP = "localhost"

ssh_password = getpass.getpass()

sshtunnel.SSH_TIMEOUT = 60 * 60 * 2  # keep the connection open 2 hours

prefect_frontend = SSHTunnelForwarder(
    (REMOTE_SERVER_IP, 22),
    ssh_username="madinsights",
    ssh_password=ssh_password,
    remote_bind_address=(PRIVATE_SERVER_IP, 8080),
    local_bind_address=('localhost', 8080)
)

prefect_graphql = SSHTunnelForwarder(
    (REMOTE_SERVER_IP, 22),
    ssh_username="madinsights",
    ssh_password=ssh_password,
    remote_bind_address=(PRIVATE_SERVER_IP, 4200),
    local_bind_address=('localhost', 4200)
)

prefect_frontend.start()
prefect_graphql.start()

print("Created tunnels")

webbrowser.open("http://localhost:8080")
