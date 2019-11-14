import subprocess

def print_green(result):
	print("\x1b[32m" + result + "\x1b[0m")

def print_red(result):
	print("\x1b[31m" + result + "\x1b[0m")

def main():
	status = subprocess.check_output("netstat -plunt", shell=True)
	check_ports(status, "0.0.0.0:5000   ", "Flask is") # White spaces to make search exact
	check_ports(status, "0.0.0.0:443    ", "SSL is")
	check_ports(status, "0.0.0.0:8080   ", "Airflow is")
	check_ports(status, "0.0.0.0:80     ", "nginx")
	check_ports(status, "0.0.0.0:5432   ", "Local postgres is")

def check_ports(status, port_to_check, message):
	if port_to_check in status:
		print_green(message + " running")
	else:
		print_red(message + " not running")

if __name__ == "__main__":
	main()
