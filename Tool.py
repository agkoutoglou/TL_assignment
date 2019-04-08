import docker

def assigment():
	try:
		client=docker.from_env()
		ListOfImages = client.images.list()
		print("list of images")
		print(ListOfImages)
		print("")
		RunningInstance = client.containers.run('pythonapp',['python','app.py'],ports={"80/tcp":4000},detach=True)
		print("Containers")
		AllContainers = client.containers.list(all=True)
		print(AllContainers)
		RunningContainer = client.containers.get(RunningInstance.id)
		print("Running Container")
		print(RunningContainer)
		print("will run for 5 minutes.")
		RunningInstance.stop(timeout=300)
		RunningInstance.wait()
		
	except docker.errors.APIError:
		nope="Not working!"

if __name__ == "__main__":
	assigment()
	print(45*"=")
	print("=Success. Tool executed successfully=")
	print(45*"=")

# Kill all running containers: docker kill $(docker ps -q)

# Remove all containers: docker rm $(docker ps -a -q)

# Sunexise me ta upoloipa - Na kanei polla containers, na kanei validate, na pairnei system metrics kai na enoipoihsei ta logs se ena 