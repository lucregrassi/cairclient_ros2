import sys

import rclpy
from rclpy.node import Node
from cair_interfaces.srv import CairSrv


class MinimalClientAsync(Node):

    def __init__(self):
        super().__init__('minimal_client_async')
        self.cli = self.create_client(CairSrv, 'cair_srv')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = CairSrv.Request()

    def send_request(self):
        self.req.sentence = input("U: ").strip()
        self.future = self.cli.call_async(self.req)


def main():
	rclpy.init()
	minimal_client = MinimalClientAsync()

	while(True):
		minimal_client.send_request()

		while rclpy.ok():
			rclpy.spin_once(minimal_client)
			if minimal_client.future.done():
				try:
					response = minimal_client.future.result()
				except Exception as e:
					minimal_client.get_logger().info('Service call failed %r' % (e,))
				else:
					reply = response.dialogue_sentence
					if response.plan_sentence:
						if response.plan:
							reply = response.plan_sentence + " " + response.plan + " " + response.dialogue_sentence
						else:
							reply = response.plan_sentence + " " + response.dialogue_sentence
					print("R:", reply)
				break

	minimal_client.destroy_node()
	rclpy.shutdown()


if __name__ == '__main__':
    main()
