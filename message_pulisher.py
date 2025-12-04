import rospy
from learning_topic.msg import person


def message_publisher():
    # Initialize the ROS node
    rospy.init_node("message_publisher", anonymous=True)

    # Create a publisher to publish the topic and message
    publisher = rospy.Publisher("/person_info", person, queue_size=10)

    # Set the rate of publisher
    publisher_rate = rospy.Rate(10) # 10HZ

    # Set the message
    while not rospy.is_shutdown():
        person_msg = person()
        person_msg.name = "Ruipu"
        person_msg.age = 24
        person_msg.sex = person.male

        # Publish this mesage
        publisher.publish(person_msg)

        # Print the info
        rospy.loginfo(f"publish the person info: Name:{person_msg.name}, Age: {person_msg.age}, Sex: {person_msg.sex}")

        # Sleep the time
        publisher_rate.sleep()

if __name__ == "__main__":
    try:
        message_publisher()

    except rospy.ROSInterruptException:
        pass