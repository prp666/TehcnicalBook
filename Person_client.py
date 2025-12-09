import rospy
from learning_service.srv import Person, PersonRequest


def person_client():

    # Initialize the ROS node
    rospy.init_node("ROS_person_client", anonymous=True)

    # Wait untile the service is available
    rospy.wait_for_service("/show_person")

    # The main action
    try:
        # Create a service proxy
        person_client_request = rospy.ServiceProxy("/show_person", Person)

        # Send the request and get the response
        response = person_client_request("Ruipu", 24, PersonRequest.male)

        # Log the response
        return response.result
    
    except rospy.ServiceException as e:

        rospy.logerr(f"Service call failed: {e}")



if __name__ == "__main__":
    
    try:
        person_client()

    except rospy.ROSInterruptException():

        pass