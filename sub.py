#!/usr/bin/env python3

import rospy 
from msg_pub_sub.msg import xyz

def add_quotes(var_value):
    quoted = '"' + var_value + '"'
    return quoted

def save_to_sh(var_name, var_val):
    path = "vars.sh"
    var_value = add_quotes(var_val)
    old_var = False

    
    with open(path,"r") as f:
        lines = f.readlines()
    
    #check whether it has already declared
    for line in lines:
        if var_name in line:
            old_var=True
            print("OLD VARIABLE!")
            break

            
    if old_var: #OLD VAR
        for index,line in enumerate(lines, start=1):
            if var_name in line:
                #get the number of the line which should be updated
                #print("BULDU:",var_name)
                line_num = index
                #print("line_num:",line_num)

        lines[line_num-1] = "export " + var_name + "=" + var_value + "\n"

        with open(path, "w") as f:
            #print("yazilacak...")
            f.writelines(lines)


    else: #NEW VAR
        with open(path, "a") as f:
            f.write(f'export {var_name}={var_value}\n')


def callback(msg):
    rospy.loginfo(f"entered -> {msg.var_name} = {msg.var_value}")
    
    save_to_sh(msg.var_name, msg.var_value)
    print("saved!")



def sub():
    rospy.init_node("sub01", anonymous=True)
    rospy.Subscriber("topic01", xyz, callback)
    rospy.spin()

if __name__ == "__main__":
    sub()

