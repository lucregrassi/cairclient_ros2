#!/usr/bin/env python
"""
Author:      Lucrezia Grassi
Email:       lucrezia.grassi@edu.unige.it
Affiliation: Laboratorium, DIBRIS, University of Genoa, Italy
Project:     CAIR

This file contains a client for the CAIR server
"""

from __future__ import print_function
import rclpy
import requests
import os
import json
from rclpy.node import Node
from cair_interfaces.srv import CairSrv

server_IP = "131.175.205.146"
BASE = "http://" + server_IP + ":5000/CAIR_hub"

class MinimalService(Node):

	def __init__(self):
		super().__init__('minimal_service')
		self.srv = self.create_service(CairSrv, 'cair_srv', self.cair_client_callback)

	def cair_client_callback(self, request, response):
		print(os.getcwd())
		if not os.path.exists("dialogue_state.json"):
			res = requests.get(BASE, verify=False)
			dialogue_state = res.json()['dialogue_state']
			# Save the client state in the file
			with open("dialogue_state.json", 'w') as f:
				json.dump(dialogue_state, f)
		else: 
			with open("dialogue_state.json", 'r') as f:
				dialogue_state = json.load(f)
		data = {"client_sentence": sentence, "dialogue_state": dialogue_state}
		encoded_data = json.dumps(data).encode('utf-8')
        	compressed_data = zlib.compress(encoded_data)
		server_resp = requests.put(BASE, data=compressed_data, verify=False)
		dialogue_state = server_resp.json()['dialogue_state']
		with open("dialogue_state.json", 'w') as f:
            		json.dump(dialogue_state, f)
		response.plan_sentence = server_resp.json()['plan_sentence']
		response.plan = server_resp.json()['plan']
		response.dialogue_sentence = server_resp.json()['dialogue_sentence']
		self.get_logger().info('Incoming sentence:%s' % request.client_sentence)
		self.get_logger().info('Plan sentence: %s' % response.plan_sentence)
		self.get_logger().info('Plan: %s' % response.plan)
		self.get_logger().info('Dialogue sentence: %s' % response.dialogue_sentence)
		return response


def main():
    rclpy.init()
    minimal_service = MinimalService()
    rclpy.spin(minimal_service)
    rclpy.shutdown()


if __name__ == '__main__':
    main()


