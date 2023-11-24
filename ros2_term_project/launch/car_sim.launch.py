#!/usr/bin/env python3
#
# Copyright 2023. Prof. Jong Min Lee @ Dong-eui University
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
from launch.actions import ExecuteProcess
import json
from launch.substitutions import LaunchConfiguration


print(os.path.realpath(__file__))

ld = LaunchDescription()


def generate_launch_description():
    # configuration
    world = LaunchConfiguration('world')
    print('world =', world)
    world_file_name = 'car_track.world'
    world = os.path.join(get_package_share_directory('ros2_term_project'),
                         'worlds', world_file_name)
    print('world file name = %s' % world)
    # ld = LaunchDescription()
    declare_argument = DeclareLaunchArgument(
        'use_sim_time',
        default_value='false',
        description='Use simulation (Gazebo) clock if true')

    gazebo_run = ExecuteProcess(
        cmd=['gazebo', '-s', 'libgazebo_ros_factory.so', world],
        output='screen')

    ld.add_action(declare_argument)
    ld.add_action(gazebo_run)

    # spawn prius_hybrid
    spawn_entity_node_pr001 = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        name='spawn_entity_pr001',
        output='screen',
        arguments=[
            '-database', 'prius_hybrid',
            '-entity', 'PR001',
            '-x', '93',
            '-y', '-11.7',
            '-Y', '-1.57'
        ]
    )
    ld.add_action(spawn_entity_node_pr001)

    spawn_entity_node_pr002 = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        name='spawn_entity_pr002',
        output='screen',
        arguments=[
            '-database', 'prius_hybrid',
            '-entity', 'PR002',
            '-x', '93',
            '-y', '-15.9',
            '-Y', '-1.57'
        ]
    )
    ld.add_action(spawn_entity_node_pr002)

    # Ackermann 드라이브 컨트롤러 추가 - PR001
    ackermann_controller_pr001 = Node(
        package='ackermann_drive_controller',
        executable='ackermann_drive_controller_node',
        name='ackermann_controller_pr001',
        output='screen',
        parameters=[
            {'use_sim_time': True},
            {'vehicle_name': 'PR001'},
            {'publish_period': 0.1},  # 필요에 따라 게시 주기 조정
        ]
    )
    ld.add_action(ackermann_controller_pr001)

    # Ackermann 드라이브 컨트롤러 추가 - PR002
    ackermann_controller_pr002 = Node(
        package='ackermann_drive_controller',
        executable='ackermann_drive_controller_node',
        name='ackermann_controller_pr002',
        output='screen',
        parameters=[
            {'use_sim_time': True},
            {'vehicle_name': 'PR002'},
            {'publish_period': 0.1},  # 필요에 따라 게시 주기 조정
        ]
    )
    ld.add_action(ackermann_controller_pr002)

    # 카메라 컨트롤러 추가 - PR001
    camera_controller_pr001 = Node(
        package='camera_controller_package',  # 카메라 컨트롤러 패키지 이름으로 수정
        executable='camera_controller_node',
        name='camera_controller_pr001',
        output='screen',
        parameters=[
            {'camera_name': 'prius_camera_pr001'},
            # 추가적인 카메라 컨트롤러 파라미터 설정
        ]
    )
    ld.add_action(camera_controller_pr001)

    # 카메라 컨트롤러 추가 - PR002
    camera_controller_pr002 = Node(
        package='camera_controller_package',  # 카메라 컨트롤러 패키지 이름으로 수정
        executable='camera_controller_node',
        name='camera_controller_pr002',
        output='screen',
        parameters=[
            {'camera_name': 'prius_camera_pr002'},
            # 추가적인 카메라 컨트롤러 파라미터 설정
        ]
    )
    ld.add_action(camera_controller_pr002)

    return ld
