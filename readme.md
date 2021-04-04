## Two Python REST services run on docker-compose

#### Describtion

There are two services run by docker-compose:
- PingService - after receiving POST request on api/v1/ping route with url it should try to reach the url via HTTP and return it's payload. 
  After receiving GET request on /healthy route it should return "healthy" string indicating it is reachable. Currently it is a plain text message and it will be optimised for real case usage in the future.
  This service is exposed on host port 8080.
- ReceiverService - after receiving GET request on api/v1/info it should return string "Receiver: Hello api2.py!". It has been created for testing purpose.

#### Usage

To run environment use command:

`docker-compose up -d`
