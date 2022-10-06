##!/usr/bin/env python3
'''
*******************************
*
*        		===============================================
*           		Krishi Bot (KB) Theme (eYRC 2022-23)
*        		===============================================
*
*  This script should be used to implement Task 0 of Krishi Bot (KB) Theme (eYRC 2022-23).
*  
*  This software is made available on an "AS IS WHERE IS BASIS".
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or 
*  breach of the terms of this agreement.
*
*******************************
'''


# Team ID:			[ eYRC#KB#1477 ]
# Author List:		[Ayush Ranjan, Priya Jha, Vedant Jain, Anushka Dwivedi]
# Filename:			task_0.py
# Functions:		
# 					[ Callback, main, Straight_move, circle_move, turn , start_move]
# Nodes:		    Add your publishing and subscribing node


####################### IMPORT MODULES #######################

import sys
from tkinter.messagebox import NO
import traceback
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
##############################################################

################# ADD GLOBAL VARIABLES HERE #################
ang = 0
y = 0
##############################################################

################# ADD UTILITY FUNCTIONS HERE #################
def turn(action,msg,pub,turn_angle):
    global ang
    a0=ang
    while abs(abs(a0)-abs(ang))<=turn_angle:
        rospy.loginfo("Turning...")
        action(pub,msg,0,1)
    action(pub,msg,0,0)
    # global y
    # print(y)

def circle_move(action,msg,pub,angle_covered):
    global ang
    a0=ang
    while abs(a0-ang)<=angle_covered-0.5:
        rospy.loginfo("Moving in circle...")
        action(pub,msg,1,1)
    action(pub,msg,0,0)
    
def start_move(pub,msg,speed_linear,speed_angular):
    msg.linear.x=speed_linear
    msg.angular.z=speed_angular
    pub.publish(msg)




def straight_move(action,msg,pub,destination_y):
    global y
    y0=y
    while abs(y0-y)<=destination_y:
        rospy.loginfo("Moving in straight line... ")
        action(pub,msg,1,0)
    action(pub,msg,0,0)
    

##############################################################
def callback(data):
	
	# Input Arguments:
    global ang,y
    ang  = data.theta*180/3.1415 
    y= data.y
	# Returns:
    # rospy.loginfo("Current angle:%f",ang)
    # rospy.loginfo("Current position y:%f",y)


def main():
	
    rospy.init_node('turtle_controller_node', anonymous=True)
    rospy.Subscriber("/turtle1/pose", Pose, callback)
   
    rospy.loginfo("Start")

    controller = rospy.Publisher('/turtle1/cmd_vel',Twist, queue_size=10)
    obj_msg = Twist()


    while not rospy.is_shutdown():
          
        circle_move(start_move,obj_msg,controller,180)
        
        turn(start_move,obj_msg,controller,90)        

        straight_move(start_move,obj_msg,controller,2)

        rospy.loginfo(">>>Task completed<<<")
        print("Exiting......")
     
        rospy.signal_shutdown("completed")

        

    # rospy.spin()
        
            
                  
######### YOU ARE NOT ALLOWED TO MAKE CHANGES TO THIS PART #########  

if __name__ == "__main__":
    try:
        print("------------------------------------------")
        print("         Program Started!!          ")
        print("------------------------------------------")
        main()

    except:
        print("------------------------------------------")
        traceback.print_exc(file=sys.stdout)
        print("------------------------------------------")
        sys.exit()

    finally:
        print("------------------------------------------")
        print("    Program Executed Successfully   ")
        print("------------------------------------------")
