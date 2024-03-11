# SensorStream-ClientServer
The communication between the client and the application (server) is carried out using the HTTP protocol. The application exposes an API that allows querying the data provided by the sensor network. The data from a specific sensor or a group of sensors can be queried. The identifier of the sensor/sensor group is sent as a parameter when calling the API. The sensors operate asynchronously. The data provided by the sensors are transmitted using the MQTT protocol to a broker-type system in the Cloud - HiveMQ. The sensors are simulated through a script that generates the corresponding data. The application runs as a Docker container. A Dockerfile is implemented for generating a Docker image.

TBE: Implement a environment variable.
