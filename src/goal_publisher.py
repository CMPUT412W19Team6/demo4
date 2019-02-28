#!/usr/bin/env python

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from sensor_msgs.msg import Joy, LaserScan

def joy_callback(msg):
    global client, goal_dict

    if msg.buttons[0] == 1:  # button A
        goal = goal_dict["A"]
        goal.target_pose.header.stamp = rospy.Time.now()

        client.send_goal(goal)

        # wait = client.wait_for_result()
        # # If the result doesn't arrive, assume the Server is not available
        # if not wait:
        #     rospy.logerr("Action server not available!")
        #     rospy.signal_shutdown("Action server not available!")
        # else:
        # # Result of executing the action
        #     if client.get_result():
        #         rospy.loginfo("Goal execution done!")


    elif msg.buttons[1] == 1:  # button B
        goal = goal_dict["B"]
        goal.target_pose.header.stamp = rospy.Time.now()

        client.send_goal(goal)

    elif msg.buttons[2] == 1:  # button X
        goal = goal_dict["X"]
        goal.target_pose.header.stamp = rospy.Time.now()

        client.send_goal(goal)
    elif msg.buttons[3] == 1:  # button Y
        goal = goal_dict["Y"]
        goal.target_pose.header.stamp = rospy.Time.now()

        client.send_goal(goal)

if __name__ == "__main__":
    rospy.init_node("goal_publisher")
    rospy.Subscriber("/joy", Joy, callback=joy_callback)

    goal1 = MoveBaseGoal()
    goal1.target_pose.header.frame_id = "map"
    goal1.target_pose.pose.position.x = 2.1849
    goal1.target_pose.pose.position.y = 0.3022
    goal1.target_pose.pose.position.z = 0.0
    goal1.target_pose.pose.orientation.x = 0.0
    goal1.target_pose.pose.orientation.y = 0.0
    goal1.target_pose.pose.orientation.z = 0.4839
    goal1.target_pose.pose.orientation.w = 0.875

    goal2 = MoveBaseGoal()
    goal2.target_pose.header.frame_id = "map"
    goal2.target_pose.pose.position.x = 2.6834
    goal2.target_pose.pose.position.y = -1.9112
    goal2.target_pose.pose.position.z = 0.0
    goal2.target_pose.pose.orientation.x = 0.0
    goal2.target_pose.pose.orientation.y = 0.0
    goal2.target_pose.pose.orientation.z = -0.2742
    goal2.target_pose.pose.orientation.w = 0.9616

    goal3 = MoveBaseGoal()
    goal3.target_pose.header.frame_id = "map"
    goal3.target_pose.pose.position.x = 4.0847
    goal3.target_pose.pose.position.y = -2.5276
    goal3.target_pose.pose.position.z = 0.0
    goal3.target_pose.pose.orientation.x = 0.0
    goal3.target_pose.pose.orientation.y = 0.0
    goal3.target_pose.pose.orientation.z = -0.2448
    goal3.target_pose.pose.orientation.w = 0.9695

    goal4 = MoveBaseGoal()
    goal4.target_pose.header.frame_id = "map"
    goal4.target_pose.pose.position.x = 4.0810
    goal4.target_pose.pose.position.y = -0.7428
    goal4.target_pose.pose.position.z = 0.0
    goal4.target_pose.pose.orientation.x = 0.0
    goal4.target_pose.pose.orientation.y = 0.0
    goal4.target_pose.pose.orientation.z = -0.4553
    goal4.target_pose.pose.orientation.w = 0.8902

    goal_dict = {
        "A": goal1,
        "B": goal2,
        "X": goal3,
        "Y": goal4
    }

    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
    client.wait_for_server()

    rospy.spin()