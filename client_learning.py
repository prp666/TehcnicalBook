import rospy
import sys
# Import the service message type, in the srv directory
from turtlesim.srv import Spawn


def spawn_turtle():
    # Initialize the ROS node
    rospy.init_node("Spawn_Turtle", anonymous=True)

    # Wait the /spawn service, while it's available, the program continues
    rospy.wait_for_service("/spawn")

    # Create the client, do settings for the client, the 
    try:

        # Method ServiceProxy() is to use the service
        spawn_turtle = rospy.ServiceProxy("/spawn", Spawn)

        # Use the object spawn_turtle to call the service and use the response
        response = spawn_turtle(2.0, 2.0, 0.0, "turtle2")

        return response.name

    except rospy.ServiceException as e:
        print(f"ROS Service call failed: {e}")
    

if __name__ == "__main__":
        
    print(f"Spwan turtle successfully, the name is {spawn_turtle()}")