# TL_assigment
Tradeline assigment


Python tool to manage and monitor Docker's containers.
The current tool creates 5 containers that runs Flask and they listen to localhost:[4000-4004] to return a web page containing a "Hello World" and the container ID.

All files are needed in the same directory and Python 3 must be installed. Execute the tool by typing:

python Tool.py

The tool will start by creating the image "pythonapp" from the Dockerfile and then will continue with creation of five containers. Each step is reporting it's status
via an stdout output and every minute the metrics of the containers along with the logs will be stored in Central.log file after the end of the tool execution.
Log entries are shown as such:

- Container name
- Container metrics
- Flask log of HTTP return codes

-BEWARE-
File "KillAllDocker.bat" is included and it will find and stop/remove all containers & images after the execution of the tool.
DO NOT RUN THE TOOL OR "KillAllDocker.bat"  ON A PRODUCTION MACHINE THAT HOSTS DOCKER CONTAINERS! YOU'VE BEEN WARNED!
-BEWARE

This tool was running in Powershell and uses:
docker.py libraries - https://github.com/docker/docker-py
Flask microframework - http://flask.pocoo.org/
Docker - https://www.docker.com/
