## Two Python REST services run with docker-compose

#### Description

There are two services run by docker-compose:
- ping-service - after receiving POST request on api/v1/ping route with the receiver-service url it should try to reach the url via HTTP and return it's payload. 

  After receiving GET request on /health route it should return "healthy" string with status code 200 indicating that the running appication is reachable. 

  Currently docker is periodically checking if service is reachable by sending requests itself. If the request returns correct status, docker displays it in the "STATUS" column of `docker ps` command - the additional information is saying that the ping-service is currently healthy (reachable by docker).

  This service is exposed on host port 8080.
- receiver-service - after receiving GET request on api/v1/info route it should return json object "{ "Receiver": "Hello api.py!" }". It has been created for testing purpose.

#### Usage

To run environment use command:

`docker-compose up -d`

When the environment is up and running, send a request to *ping-service*:

`curl -X POST http://localhost:8080/api/v1/ping -H "Content-Type: application/json" -d '{"url":"http://receiver-service:8080/api/v1/info"}'`

Request above posts a request data to *ping-service* which then sends it to *receiver-service* as GET request.
If working correctly, it returns a json object ***{ "Receiver": "Hello api.py!"}***

#### Future

TBD
