---
layout: page
title: Robotics & Autonomy
description: Perception, Planning, Controls
img: assets/img/ROB1.jpg
importance: 3
category: work
---

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/ROB_main.png" title="main" class="img-fluid rounded z-depth-1" %}
    </div>
</div>


Creating a fully autonomous vehicle or robotic system involves integrating several crucial components. These include the perception system, path planning, trajectory generation, follower subsystem, and controls subsystem.

The perception subsystem relies on sensors like cameras, LiDARs, and RADARS to perceive the environment, localize the vehicle or robot, and plan trajectories while ensuring collision avoidance. It serves as a fundamental component for autonomous navigation.

The path planning module is responsible for generating the trajectory for the vehicle or robot to follow towards its destination. It considers objects detected by the perception system and plans to avoid collisions or getting too close to obstacles. This module utilizes a predefined map to understand constraints such as one-way roads and non-drivable areas, enabling it to plan a global path to the destination.

Lastly, the controls module issues commands to actuate and steer the vehicle or robot along the planned trajectory. Typically, separate controllers manage longitudinal and lateral movements, with one controlling throttle or brake, and the other steering the vehicle.

Below sections showcase implementations of such systems, incorporating some or all of these key components essential for autonomous navigation.

<div style="text-align: center;">
    <a href="https://github.com/omkarchittar/manipulator_control_DDPG">Reinforcement Learning Manipulator Control</a>
    <div class="container">
        <div class="row">
            <a href="https://github.com/omkarchittar/manipulator_control_DDPG" style="display: inline-block; margin: 0 auto;">
                {% include figure.liquid path="assets/img/ROB7.gif" title="Reinforcement Learning Manipulator Control 1000 ep" class="img-fluid rounded z-depth-1" %}
            </a>
        </div>
    </div>
</div>


<div class="row">
    <div class="row justify-content-center">
        <div class="col-sm mt-3 mt-md-0"><a href="https://github.com/omkarchittar/Structure_from_Motion">Structure from Motion
            {% include figure.liquid path="assets/img/SFM_square.png" title="SfM" class="img-fluid rounded z-depth-1" %}</a>
        </div>
        <div class="col-sm mt-3 mt-md-0"><a href="https://github.com/omkarchittar/LiDAR_SLAM">LiDAR SLAM
            {% include figure.liquid path="assets/img/CVDL4.png" title="LiDAR SLAM" class="img-fluid rounded z-depth-1" %}</a>
        </div>
    </div>
</div>

<div class="row">
    <div class="row justify-content-center">
        <div class="col-sm mt-3 mt-md-0"><a href="https://github.com/omkarchittar/Dijkstra_Point_Robot">Dijkstra Path Planning
            {% include figure.liquid path="assets/img/ROB3.png" title="Dijkstra Path Planning" class="img-fluid rounded z-depth-1" %}</a>
        </div>
        <div class="col-sm mt-3 mt-md-0"><a href="https://github.com/omkarchittar/A_Star_Path_Planning">A* Path Planning
            {% include figure.liquid path="assets/img/ROB4.png" title="A* Path Planning" class="img-fluid rounded z-depth-1" %}</a>
        </div>
    </div>
</div>

<div class="row">
    <div class="col-sm mt-3 mt-md-0"><a href="https://github.com/omkarchittar/Obstacle_Avoidance_Bot">Obstacle Avoiding Bot
        {% include figure.liquid path="assets/img/ROB2.png" title="Obstacle Avoiding Bot" class="img-fluid rounded z-depth-1" %}</a>
    </div>
</div>

<div class="row">
    <div class="col-sm mt-3 mt-md-0"><a href="https://github.com/omkarchittar/Wall_Following_Robot">Wall Following Bot
    {% include figure.liquid path="assets/img/ROB5.png" title="Pose Estimation" class="img-fluid rounded z-depth-1" %}</a>
    </div>
</div>

