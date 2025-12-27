import rospy
from test_subscriber_publisher.msg import Test_subscribe
import time


def publisher():
    # Initialize the ROS node
    rospy.init_node("test_publisher", anonymous=True)

    # Create the publisher
    publisher = rospy.Publisher("/test_subscriber", Test_subscribe, queue_size=10)

    # Set the publishing rate 
    rate = rospy.Rate(50)

    req = 0

    while not rospy.is_shutdown():
        msg = Test_subscribe()
        msg.seq = req
        msg.t_send = time.time()

        # Publishe the message
        publisher.publish(msg)
        req += 1
        rate.sleep()


if __name__ == "__main__":
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass