@ Kill all running containers: docker kill $(docker ps -q)

@ Remove all containers: docker rm $(docker ps -a -q)

@ Remove all images: docker rmi -f $(docker images -q)

PowerShell.exe -Command "docker kill $(docker ps -q)"

PowerShell.exe -Command "docker rm $(docker ps -a -q)"

PowerShell.exe -Command "docker rmi -f $(docker images -q)"