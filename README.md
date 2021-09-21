# ROS2 wrapper for the CAIR client
This repository contains two ROS2 packages:
* The **cair_client** Python package contains:
  * The _cair_srv_ service that connects to the CAIR server, performs a request and returns the response. The service takes a string (the user sentence) and returns three strings (the intent reply, the plan, and the actual reply).
  * The _cair_client_ node that serves as an example of how to interact with the server exploiting the developed service. The node takes the user input, calls the service and displays the response.
* The **cair_interfaces** C++ package contains the service type.

