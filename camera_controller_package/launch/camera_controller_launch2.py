from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='camera_controller_package',
            executable='camera_controller_node',
            name='camera_controller',
            output='screen',
            parameters=[{'camera_name': 'prius_camera_pr002'}],  # Adjust parameters as needed
        )
    ])
