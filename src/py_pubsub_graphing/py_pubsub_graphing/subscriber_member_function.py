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

# non-ros dependencies
import matplotlib.pyplot as plt 
import matplotlib.animation as animate


class RandomValueSubscriber(Node):

    def __init__(self):
        super().__init__('random_value_subscriber')
        self.subscription = self.create_subscription(
                Int64,
                'random',
                self.listener_callback,
                10
                )
        self.subscription  # prevent unused variable warning
        self.i = 0
        # data from talker
        self.vals = []
        self.times = []

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%d"' % msg.data)

        self.vals.append(msg.data)
        self.times.append(self.i)

        while len(self.vals) > 30:
            self.vals.pop(0)
        while len(self.times) > 30:
            self.times.pop(0)

        self.i += 1


#graphing plots
def animate(i, minimal_subscriber):
    rclpy.spin_once(minimal_subscriber)


    ax1.clear()
    ax1.plot(xs, ys)

def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = RandomValueSubscriber()

    fig = plt.figure()
    ax1 = fig.add_subplot(1,1,1)
   
    while 1:
        rclpy.spin_once(minimal_subscriber)

        print(minimal_subscriber.vals)
        ax1.clear()
        ax1.plot(minimal_subscriber.times, minimal_subscriber.vals)

    #rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    plt.show()
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
