import rospy
from turtlesim.msg import Pose


# Calllback funtion, used while receiving message then process this message
def pose_callback(pose_msg):
    rospy.loginfo(f"Turtle Pose: Speed linear x: {pose_msg.x}, y: {pose_msg.y}")


# The main function
def pose_subscriber():
    # Initialize the ROS node
    rospy.init_node("pose Subscriber", anonymous=True)

    # Create a subscriber, this is a listener, while we initialized this listener, it will keep listening
    # then automatically send the message it received to the callback function as the parameter
    rospy.Subscriber("turtle1/pose", Pose, pose_callback)

    # Keep the program alive until interrupted, not keep everything running in loop, every code run once
    rospy.spin()

if __name__ == "__main__":
    try:
        pose_subscriber()

    except rospy.ROSInterruptException:
        pass