# TL_assigment
Tradeline assigment


Python tool to manage and monitor Docker's containers.
The current tool creates 5 containers that runs Flask and they listen to localhost:[4000-4004] to return a web page containing a "Hello World" and the container ID.

All files are needed in the same directory and Python 3 must be installed. Execute the tool by typing:

python Tool.py

The tool will start by creating the image "pythonapp" from the Dockerfile and then will continue with creation of five containers. Each step is reporting it's status
via an stdout output and every minute the metrics of the containers along with the logs will be stored in Central.log file after the end of the tool execution.
Log entries are shown as such:

=============NEW LOG ENTRY=============
Container happy_taussig
Start of operation performance status ----->>>{'read': '2019-04-10T23:35:57.3579612+02:00', 'preread': '2019-04-10T23:35:56.3539611+02:00', 'pids_stats': {}, 'blkio_stats': {'io_service_bytes_recursive': None, 'io_serviced_recursive': None, 'io_queue_recursive': None, 'io_service_time_recursive': None, 'io_wait_time_recursive': None, 'io_merged_recursive': None, 'io_time_recursive': None, 'sectors_recursive': None}, 'num_procs': 8, 'storage_stats': {'read_count_normalized': 15, 'read_size_bytes': 41984, 'write_count_normalized': 1223, 'write_size_bytes': 9957376}, 'cpu_stats': {'cpu_usage': {'total_usage': 14522415, 'usage_in_kernelmode': 0, 'usage_in_usermode': 0}, 'throttling_data': {'periods': 0, 'throttled_periods': 0, 'throttled_time': 0}}, 'precpu_stats': {'cpu_usage': {'total_usage': 14517943, 'usage_in_kernelmode': 0, 'usage_in_usermode': 0}, 'throttling_data': {'periods': 0, 'throttled_periods': 0, 'throttled_time': 0}}, 'memory_stats': {'commitbytes': 1082445824, 'commitpeakbytes': 1083236352, 'privateworkingset': 246521856}, 'name': '/happy_taussig', 'id': '3e08096bbeff3be73c10cc6c084f2551f05bb6b8b36a6e940996ecccd77b8918', 'networks': {'79903E82-7DAA-491E-B90F-05EEADBC69DF': {'rx_bytes': 13948, 'rx_packets': 97, 'rx_errors': 0, 'rx_dropped': 1, 'tx_bytes': 2982, 'tx_packets': 36, 'tx_errors': 0, 'tx_dropped': 0}}} <<<-------- This is the end of operation performance status
Below is the log of Flask running in the container
b'2019-04-10T21:33:02.444499400Z  * Serving Flask app "app" (lazy loading)\n2019-04-10T21:33:02.444499400Z  * Environment: production\n2019-04-10T21:33:02.444499400Z    WARNING: Do not use the development server in a production environment.\n2019-04-10T21:33:02.444499400Z    Use a production WSGI server instead.\n2019-04-10T21:33:02.444988800Z  * Debug mode: off\n2019-04-10T21:33:02.492987200Z  * Running on http://0.0.0.0:80/ (Press CTRL+C to quit)\n2019-04-10T21:33:18.177559000Z 192.168.0.2 - - [10/Apr/2019 21:33:17] "GET / HTTP/1.1" 200 -\n2019-04-10T21:33:18.418557300Z 192.168.0.2 - - [10/Apr/2019 21:33:18] "GET /favicon.ico HTTP/1.1" 404 -\n'


-BEWARE-
File "KillAllDocker.bat" is included and it will find and stop/remove all containers & images after the execution of the tool.
DO NOT RUN THE TOOL OR "KillAllDocker.bat"  ON A PRODUCTION MACHINE THAT HOSTS DOCKER CONTAINERS! YOU'VE BEEN WARNED!
-BEWARE

This tool was running in Powershell and uses:
docker.py libraries - https://github.com/docker/docker-py
Flask microframework - http://flask.pocoo.org/
Docker - https://www.docker.com/
