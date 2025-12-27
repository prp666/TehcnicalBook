#!/usr/bin/env python3
import rospy
import time
from test_latency_loss.srv import Test_service, Test_serviceResponse

SERVICE_NAME = "/test_latency_loss"

def client():
    rospy.init_node("test_client", anonymous=True)

    # Wait until the service becomes available
    rospy.loginfo("[CLIENT] Waiting for service %s ...", SERVICE_NAME)
    rospy.wait_for_service(SERVICE_NAME)

    # Create service proxy
    proxy = rospy.ServiceProxy(SERVICE_NAME, Test_service)
    rospy.loginfo("[CLIENT] Service connected")

    # Test parameters
    N = 100                 # number of requests
    SLEEP = 0.05            # interval between requests (seconds)

    success = 0
    lost = 0
    rtts_ms = []

    for i in range(N):
        t_start = time.time()
        try:
            # Call service (field name must match .srv: t_send)
            response = proxy.call(t_send=t_start)

            rtt_ms = (time.time() - t_start) * 1000.0
            rtts_ms.append(rtt_ms)
            success += 1

            print(f"[OK] seq={i} RTT={rtt_ms:.2f} ms")

        except rospy.ServiceException as e:
            lost += 1
            print(f"[LOST] seq={i} ServiceException: {e}")

        except Exception as e:
            lost += 1
            print(f"[LOST] seq={i} Exception: {e}")

        time.sleep(SLEEP)

    # Summary
    print("\n===== TEST RESULT =====")
    if rtts_ms:
        avg_rtt = sum(rtts_ms) / len(rtts_ms)
        print(f"Average RTT: {avg_rtt:.2f} ms")

    print(f"Total requests: {N}")
    print(f"Successful calls: {success}")
    print(f"Lost calls: {lost}")
    print(f"Loss rate: {(lost / N) * 100:.2f}%")

if __name__ == "__main__":
    client()
