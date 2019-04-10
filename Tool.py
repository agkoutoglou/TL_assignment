#################################
##  Assigment for TradeLine    ##
##  Author: Robert Agkoutoglou ##
#################################

import docker, time, subprocess, sys

# Static variables
image_name="pythonapp"
docker_client=docker.from_env()
monitor_interval_per_min = 1

#Methods
def clear_images_containers(): # Run KillAllDocker batch file to clear up everything
	p = subprocess.Popen(["powershell.exe", 
              ".\\KillAllDocker"], 
              stdout=sys.stdout)
	p.communicate()
	
def get_current_time():	# Returns system time
	time_track = time.localtime()
	time_track_report = time.strftime("%m/%d/%Y, %H:%M:%S", time_track)
	return time_track_report
		
def create_image(): # Image creation from Dockerfile
	print("Creating image \"pythonapp\" from Dockerfile")
	docker_image = docker_client.images.build(path="./",tag=image_name)
	list_of_images = docker_client.images.list()
	print("List of images:")
	print(list_of_images)
	print("")
		
def create_containers(): # Creates 5 containers and binds TCP ports [4000-4004]
	print("Creating containers at " + get_current_time())
	running_instances = []
	running_containers = []
	for index in range(5):
		port_number = 4000 + index
		running_instances.append(docker_client.containers.run(image_name,['python','app.py'],ports={"80/tcp":port_number},detach=True,remove=True))
		running_containers.append(running_instances[index].id)
		#print("Started container " + running_containers[index] + " which listens to port No:" + str(port_number))
		print("Started container " + running_instances[index].name + " which listens to port No:" + str(port_number))
	print("")
	return running_containers
		
def stop_remove_containers(list_of_containers): # Stopping of the containers
	print("Stopping and removing containers at " + get_current_time())
	for index in list_of_containers:
		print("Stopping " + docker_client.containers.get(index).name)
		docker_client.containers.get(index).stop()
	print("")

def remove_image(name_of_image): # Removal of the image
	print("Removing images at " + get_current_time())
	docker_client.images.remove(image=name_of_image,force=True)
	print("")

def keep_logs_and_wait(minutes,list_of_containers): # Keeps logs and keeps the containers in running state
	central_log_file = open("Central.log","w+")
	# The loops are counting how many minutes we set the runtime and in each one minute how many times to dump stats and logs in Central.log file
	for minute in range(minutes):
		time_counter = 0
		while time_counter < 60:
			for index in list_of_containers:
				central_log_file.write("\n" + 13*"=" + "NEW LOG ENTRY" + 13*"=" + "\n" + "Container " + str(docker_client.containers.get(index).name) + "\n" + str(docker_client.containers.get(index).stats(stream=False)) + "\n" + str(docker_client.containers.get(index).logs(timestamps=True)) + "\n")
			time.sleep(60 / monitor_interval_per_min)
			time_counter += 60 / monitor_interval_per_min
		print(str(minute+1) + " passed at " + get_current_time())
	central_log_file.close
	
def Assigment(): # "Main" function
	try:
		print("Initiating tool at " + get_current_time())
		print("")
		# Creation of the image "pythonapp"
		create_image()
		# Creation of the flask containers with random names
		running_containers = create_containers()
		# Prints the status of the containers. Must be "running"
		for index in running_containers:
			print("First container: " +  docker_client.containers.get(index).status)
		print("will run for 5 minutes.")
		# Keeping the containers in operational state for 5 minutes and direct all logs to Central.log file
		keep_logs_and_wait(5,running_containers)
		# After 5 minutes, stop the containers
		stop_remove_containers(running_containers)
		# Remove of the image "pythonapp"
		remove_image(image_name)
		print("")
		print("Tool operation completed at " + get_current_time())
		
	except docker.errors.APIError as not_working_error:
		print (not_working_error.message)
		clear_images_containers()

if __name__ == "__main__": # Execution of "main" function and prints a success message
	Assigment()
	print(39*"=")
	print("= Success. Tool executed successfully =")
	print(39*"=")
	clear_images_containers()
