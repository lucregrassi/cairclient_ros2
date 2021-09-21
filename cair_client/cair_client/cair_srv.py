#!/usr/bin/env python

from __future__ import print_function
import rclpy
import requests
import os
import pickle
import json
from rclpy.node import Node
from cair_interfaces.srv import CairSrv

cineca = "131.175.198.134"
BASE = "http://" + cineca + ":5000/"

class MinimalService(Node):

	def __init__(self):
		super().__init__('minimal_service')
		self.srv = self.create_service(CairSrv, 'cair_srv', self.cair_client_callback)

	def cair_client_callback(self, request, response):
		print(os.getcwd())
		if not os.path.exists("state.txt"):
			res = requests.put(BASE + "CAIR_server", verify=False)
			client_state = res.json()['client_state']
			# Save the client state in the file
			with open("state.txt", 'wb') as f:
				pickle.dump(client_state, f)
		else: 
			with open("state.txt", 'rb') as f:
				client_state = pickle.load(f)
		server_resp = requests.get(BASE + "CAIR_server/" + request.sentence, data=json.dumps(client_state), verify=False)
		client_state = server_resp.json()['client_state']
		with open("state.txt", 'wb') as f:
            		pickle.dump(client_state, f)
		response.intent_reply = server_resp.json()['intent_reply']
		response.plan = server_resp.json()['plan']
		response.reply = server_resp.json()['reply']
		self.get_logger().info('Incoming sentence:%s' % request.sentence)
		self.get_logger().info('Intent reply: %s' % response.intent_reply)
		self.get_logger().info('Plan: %s' % response.plan)
		self.get_logger().info('Reply: %s' % response.reply)
		return response


def main():
    rclpy.init()
    minimal_service = MinimalService()
    rclpy.spin(minimal_service)
    rclpy.shutdown()


if __name__ == '__main__':
    main()


