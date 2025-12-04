#!/usr/bin/env python3

# The line above is used to specify the interpreter for ROS, bu we can use the python xxxx to running


import rospy
from learning_topic.msg import person


def callback(person_msg):
    rospy.loginfo(f"Received person info: Name:{person_msg.name}, Age: {person_msg.age}")


def message_subscriber():
    # Initialize the ROS node
    rospy.init_node("message_subscriber", anonymous=True)

    # Create a subscriber to listen the topic and the message
    rospy.Subscriber("/person_info", person, callback)

    # Keep the program alive until interrupted by the keyboard
    rospy.spin()


if __name__ == "__main__":
    try:
        message_subscriber()

    except rospy.ROSInterruptException:
        pass
