#!/usr/bin/env python3

import rospy 
from msg_pub_sub.msg import xyz

def pub():

    pub = rospy.Publisher("topic01", xyz)
    rospy.init_node("pub01", anonymous=True)

    r = rospy.Rate(10)

    #tüm girilenler
    words = input("Enter env var:")

    splitter="=" #eşitirin önünde arkasında boşluksuz girildiyse
    var_name = words.partition(splitter)[0]
    var_value = words.partition(splitter)[2]

    msg = xyz()
    msg.var_name = var_name
    msg.var_value = var_value
    pub.publish(msg)
    
    rospy.sleep(0.1)

    while not rospy.is_shutdown():
        #rospy.loginfo(words)
        r.sleep()


if __name__ == "__main__":
    try:
        pub()
    except rospy.ROSInterruptException:
        pass 