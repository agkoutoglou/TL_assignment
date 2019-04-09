import docker
import time

image_name="pythonapp"
docker_client=docker.from_env()

def get_current_time():	
		time_track = time.localtime()
		time_track_report = time.strftime("%m/%d/%Y, %H:%M:%S", time_track)
		return time_track_report
		
def create_image():
		docker_image = docker_client.images.build(path="./",tag=image_name)
		list_of_images = docker_client.images.list()
		print("List of images:")
		print(list_of_images)
		print("")
		return docker_image
		
def create_containers():		
		RunningInstance = docker_client.containers.run(image_name,['python','app.py'],ports={"80/tcp":4000},detach=True,remove=True)
		SecondRunningInstance = docker_client.containers.run(image_name,['python','app.py'],ports={"80/tcp":4001},detach=True,remove=True)
		print("List of containers:")
		all_containers_list = docker_client.containers.list(all=True)
		print(all_containers_list)
		RunningContainer = docker_client.containers.get(RunningInstance.id)
		SecondRunningContainer = docker_client.containers.get(SecondRunningInstance.id)
		print("Creating containers at " + get_current_time())
		print(RunningContainer)
		print(SecondRunningContainer)
		print("")
		return [RunningContainer, SecondRunningContainer]
		
def stop_remove_containers(list_of_containers):
		print("Stopping and removing containers at " + get_current_time())
		list_of_containers[0].stop()
		list_of_containers[1].stop()
		print("")

def remove_image(name_of_image):
		print("Removing images at " + get_current_time())
		docker_client.images.remove(image=name_of_image,force=True)
		print("")
	
def Assigment():
	try:
		print("Initiating tool at " + get_current_time())
		print("")
		create_image()
		running_containers = create_containers()
		print("will run for 5 minutes.")
		time.sleep(30)#NA ALLAKSEI SE 300
		stop_remove_containers(running_containers)
		remove_image(image_name)
		print("")
		print("Tool operation completed at " + get_current_time())
		
	except docker.errors.APIError:
		nope="Not working!"

if __name__ == "__main__":
	Assigment()
	print(39*"=")
	print("= Success. Tool executed successfully =")
	print(39*"=")

# Kill all running containers: docker kill $(docker ps -q)

# Remove all containers: docker rm $(docker ps -a -q)

# Remove all images: docker rmi -f $(docker images -q)

# Sunexise me ta upoloipa - Na kanei polla containers, na kanei validate, na pairnei system metrics kai na enoipoihsei ta logs se ena 
# 8elei na doulepsei ligo to 8ema tou remove_image() (this. ?) an 8a parei string h image