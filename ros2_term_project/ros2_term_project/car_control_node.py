
import rclpy
from std_msgs.msg import String


def main(args=None):
    rclpy.init(args=args)

    node = rclpy.create_node('car_control_node')
    publisher = node.create_publisher(String, '/start_car', 10)

    msg = String()
    msg.data = 'PR001'  # 'PR001' 또는 'PR002'로 변경하여 원하는 차량을 선택

    timer_period = 1  # seconds
    timer = node.create_timer(timer_period, lambda _: publisher.publish(msg))

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()