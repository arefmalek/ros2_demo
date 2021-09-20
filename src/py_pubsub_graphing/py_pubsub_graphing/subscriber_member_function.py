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


fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

times = []
vals = []


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
        ani = animate.FuncAnimation(fig, self.listener_callback,
                    interval=1000)
        plt.show(block=False)
 
    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%d"' % msg.data)


        vals.append(msg.data)
        times.append(self.i)

        print(vals, times)
        if len(vals) > 30:
            vals.pop(0)
        if len(times) > 30:
            times.pop(0)

        ax1.clear()
        ax1.plot(times, vals)

        self.i += 1

def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = RandomValueSubscriber()

    rclpy.spin(minimal_subscriber)
 
    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
