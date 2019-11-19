from subprocess import CalledProcessError, check_output
from os import path
from yaml import safe_load as yaml_load

EMPTY_SPACES = "    "
def print_green(result):
    print("\x1b[32m" + result + "\x1b[0m")

def print_red(result):
    print("\x1b[31m" + result + "\x1b[0m")

def check_service_status(status, port_to_check, message):
    if port_to_check in status:
	    print_green(message + " is running")
    else:
	    print_red(message + " is not running")

def check_script_status(file_location, message):
    if path.exists(file_location):
        print_green(message + " file exists.")
    else:
        print_red(message + " file doesn't exist.")

def check_status():
    config = yaml_load(open("service_lists.yml"))
    for script, script_location in config["files"].items():
        check_script_status(script_location, script)
    try:
	    status = check_output("netstat -plunt", shell=True)
    except CalledProcessError as identifier:
	    print("Please install netstat to run this service.")
	    return

    for service_name, port in config["services"].items():
        check_service_status(status, port + EMPTY_SPACES, service_name + " is")


if __name__ == "__main__":
    check_status()
