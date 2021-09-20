#!/usr/bin/env python3

# Copyright 2016 Open Source Robotics Foundation, Inc.
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

import rclpy
from rclpy.node import Node

from std_msgs.msg import String

from example_interfaces.msg import Int64
import random

class RandomValuePublisher(Node):

    def __init__(self):
        super().__init__('random_value_generator')
        self.publisher_ = self.create_publisher(
                Int64, 'random', 10
                )
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.publish_random)
        self.i = 0

    def publish_random(self):
        val = random.randint(20,30)
        msg = Int64()
        msg.data = val
        self.publisher_.publish(msg)
        self.i += 1

def main(args = None):
    rclpy.init(args=args)
    node = RandomValuePublisher()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
