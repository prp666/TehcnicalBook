import rospy
import time
from test_subscriber_publisher.msg import Test_subscribe


# Define the last sequence number and the counter
last_seq = None
loss = 0 

def callback(msg):
    global last_seq, loss

    t_receive = time.time()
    seq = msg.seq
    latency_ms = (t_receive - msg.t_send) * 1000

    if last_seq is not None and seq > last_seq + 1:
        loss += (seq - last_seq - 1)

    last_seq = seq

    rospy.loginfo(f"Received {seq} packages, Latency: {latency_ms:.2f} ms, Loss: {loss} packages")
    


def subscriber():
    # Initialize the ROS node
    rospy.init_node("test_subscriber", anonymous=True)

    # Create the subscriber
    rospy.Subscriber("/test_subscriber", Test_subscribe, callback)

    # Keep the program alive until interrupted
    rospy.spin()


if __name__ == "__main__":
    try:
        subscriber()

    except rospy.ROSInterruptException:
        pass