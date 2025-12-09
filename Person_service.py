import rospy
from learning_service.srv import Person, PersonResponse


# Callback function for handling the service request
def handle_request(msg):
    
    # Take the name and the age then the sex from the request message
    name = msg.name
    age = msg.age
    sex = msg.sex

    # print them on the terminal and log it inside the info
    rospy.loginfo(f"Received the following results: Name:{name}, Age:{age}, Sex:{sex}")

    # Mandatory to return the response message
    return PersonResponse("Finished")


# Funtion of server
def person_service_server():
    
    # Initialize the ROS node
    rospy.init_node("ROS_person_server", anonymous=True)

    # Define the service
    service = rospy.Service("/show_person", Person, handle_request)

    # print the info
    print("Service has been up and running, waiting the client's request")

    # Keep the program alive
    rospy.spin()

if __name__ == "__main__":

    try:
        person_service_server()

    except rospy.ROSInterruptException():

        pass