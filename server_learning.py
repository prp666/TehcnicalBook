import rospy
import threading, time
from geometry_msgs.msg import Twist
from std_srvs.srv import Trigger, TriggerResponse


# Set the state and the global publisher(Service only changes the state, still need publish the velocity)
is_moving = False
turtle_vel_publisher = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)


# The function to publish the velocity
def turtle_publisher():

    # To emphasize the is_moving is a global variable
    global is_moving

    # Keep publishing the velocity
    while True:
        if is_moving:
            vel_msg = Twist()
            vel_msg.linear.x = 0.5
            vel_msg.angular.z = 0.2
            turtle_vel_publisher.publish(vel_msg)
        
        time.sleep(0.1)

# The callback function for the service
def call_back_service(req):

    # In puthon, all the global variable need to be declared as global in function
    global is_moving
    
    # Every time the service is called, change the state
    is_moving = not is_moving
    
    # If the state is moving, start the publishing thread

    rospy.loginfo("Received request to change the service state")

    # Return the Trigger response, it required to return this, according to the service definition file
    return TriggerResponse(1, "Successfully changed the turtle's state")



# define the main process of this server
def main_server():

    # Initialize the ROS node
    rospy.init_node("service_server", anonymous=True)

    # Define the service and store it as a variable
    service = rospy.Service("/turtle_command", Trigger, call_back_service)

    # Print the info
    print("Service has been created, waiting for the client's request")

    # Create another thread to publish the velocity, in python ROS only one thread can publish the topics
    # The daemon=True means while the main program ends, this thread ends too
    s = threading.Thread(target=turtle_publisher, daemon=True)
    s.start()

    # Keep the program alive until we interrupted
    rospy.spin()


if __name__ == "__main__":
    
    try:
        main_server()

    except rospy.ROSInterruptException:
        pass
