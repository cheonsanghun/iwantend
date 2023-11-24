#!/usr/bin/env python3

import rclpy
from rclpy.node import Node


class CameraControllerNode(Node):
    def __init__(self):
        super().__init__('camera_controller_node')


def main(args=None):
    rclpy.init(args=args)
    node = CameraControllerNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
