import rospy
import sys
from std_srvs.srv import Empty


# The whole function
def get_set_parameters():

    # Initialize the ROS node
    rospy.init_node("get_set_parameters", anonymous=True)

    # get the parameter we have been used here
    blue = rospy.get_param("/turtlesim/background_b")
    green = rospy.get_param("/turtlesim/background_g")
    red = rospy.get_param("/turtlesim/background_r")

    # print the parameters before setting
    rospy.loginfo(f"Before setting, the parameters are: Blue:{blue}, Green:{green}, Red:{red}")

    # set the parameters we want
    rospy.set_param("/turtlesim/background_b", 255)
    rospy.set_param("/turtlesim/background_g", 100)
    rospy.set_param("/turtlesim/background_r", 100)

    rospy.loginfo("Parameters have been set successfully")

    # Wait the service to reset the setting
    rospy.wait_for_service("/clear")

    try:
        # Create service proxy
        service = rospy.ServiceProxy("/clear", Empty)

        # call the service, take the response
        response = service()

    except rospy.ServiceException as e:
        rospy.logerr(f"Something wrong with this error: {e}")



if __name__ == "__main__":

    try:
        get_set_parameters()

    except rospy.ROSInterruptException:
        pass