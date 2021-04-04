## Two Python REST services run on docker-compose

#### Describtion

There are two services run by docker-compose:
- ping-service - after receiving POST request on api/v1/ping route with the receiver-servie url it should try to reach the url via HTTP and return it's payload. 

  After receiving GET request on /health route it should return "healthy" string indicating that the running appication is reachable. 

Currently it is a plain text message and it will be optimised for real case usage in the future.
  
This service is exposed on host port 8080.
- receiver-service - after receiving GET request on api/v1/info route it should return string "Receiver: Hello api.py!". It has been created for testing purpose.

#### Usage

To run environment use command:

`docker-compose up -d`

When the environment is up and running, send a request to *ping-service*:

`curl -X POST http://localhost:8080/api/v1/ping -H "Content-Type: application/json" -d '{"url":"http://receiver-service:8080/api/v1/info"}'`

Request above posts a request data to *ping-service* which then sends it to *receiver-service* as GET request.
If working correctly, it returns a json response "*** { "Receiver": "Hello api.py!"} ***"

#### Future

Health check implementation:

`curl -X GET http://localhost:8080/health`

Response above will return current application health status based on service ability to perform other requests.
