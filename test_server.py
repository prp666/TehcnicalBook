import rospy
import time
from test_latency_loss.srv import Test_service, Test_serviceResponse


# handler to send back the response
def handle(req):
    return Test_serviceResponse(t_receive=time.time())



def main_server():

    # Create a ROS node for server
    rospy.init_node("test_server", anonymous=True)

    # Define the service 
    service = rospy.Service("/test_latency_loss", Test_service, handle)

    # print the info
    print("Testing the lantency and the loss")

    # keep the program alive
    rospy.spin()


if __name__ == "__main__":
    try:
        main_server()

    except rospy.ROSInterruptException:
        pass
