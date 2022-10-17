# ROS2 wrapper for the CAIR client
This repository contains two ROS2 packages:
* The **cair_client** Python package contains:
  * The _cair_srv_ service that connects to the CAIR server, performs a request and returns the response. The service takes a string (the user sentence) and returns three strings (the plan sentence, the plan, and the actual dialogue reply).
  * The _cair_client_ node that serves as an example of how to interact with the server exploiting the developed service. The node takes the user input, calls the service and displays the response.
* The **cair_interfaces** C++ package contains the service type.

For the current list of Intents with their plan and corresponding parameters consult Chapter 2.1 of the following guide: [CAIR_Developer_Guide_Plans.pdf](https://github.com/lucregrassi/CAIRclient_ROS2/files/7203728/CAIR_Developer_Guide_Plans.pdf)


