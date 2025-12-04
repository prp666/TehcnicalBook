# This scirpt pulishes velocity turtle1/cmd_vel, and the message type is: geometry_msgs::Twist 


import rospy
from geometry_msgs.msg import Twist


def velocity_publisher():
    # Initialize the ROS node
    rospy.init_node("velocity_publisher", anonymous=True)

    # Create a publisher to pulish topic as message: geometry_msgs::Twist, then has line buffer 10
    turtle_vel_pub = rospy.Publisher("/turtle1/cmd_vel", Twist,queue_size=10)

    # Set the loop publish rate
    rate = rospy.Rate(10) # 10HZ

    # Create message data
    while not rospy.is_shutdown():
        vel_msg = Twist()
        vel_msg.linear.x = 0.5
        vel_msg.angular.z = 0.2
        speed = vel_msg.linear.x
        angular = vel_msg.angular.z

    # Publish the message
        turtle_vel_pub.publish(vel_msg)

    # Log info for terminal
        rospy.loginfo(f"Publishing Velocity command: Speed {speed}m/s, Angular {angular}rad/s")

    # Sleep to maintain the loop rate
        rate.sleep()

if __name__ == "__main__":
    try:
        velocity_publisher()
        
    except rospy.ROSInterruptException:
        pass