#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from math import pi

def main():
	rospy.init_node('mynode', anonymous=False)
	rospy.Rate(1)

	pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=None, latch=True)

	pentagon_size = 2

	rospy.sleep(2)

	for i in range(5):
		move(pub, (pentagon_size, 0, 0))
		move(pub, (0, 0, pi*0.4))

def move(pub_node, pose):
	msg = Twist()

	msg.linear.x = pose[0]
	msg.linear.y = pose[1]
	msg.angular.z = pose[2]

	t0 = rospy.get_time()

	while rospy.get_time() - t0 < 1:
		pub_node.publish(msg)

	pub_node.publish(Twist())

if __name__=="__main__":
	try:
		if not ['/turtle1/pose', 'turtlesim/Pose'] in rospy.get_published_topics():
			print("ERROR: 'turtlesim' is not running. Please start 'turtlesim' to execute this script.")
			exit()

		main()

	except rospy.ROSInterruptException:
		pass