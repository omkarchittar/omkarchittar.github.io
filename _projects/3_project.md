---
layout: page
title: Robotics & Autonomy
description: Perception, Planning, Controls
img: assets/img/ROB1.jpg
importance: 3
category: earlier-work
project_gallery: true
---

<p class="gallery-back"><a href="{{ '/projects/' | relative_url }}">← All projects</a></p>

{% include gallery_figure.liquid path="assets/img/ROB_main.png" title="Autonomous system architecture" caption="Perception, localization, planning, and control in an autonomous system." overview=true %}

Creating a fully autonomous vehicle or robotic system involves integrating several crucial components. These include the perception system, path planning, trajectory generation, follower subsystem, and controls subsystem.

The perception subsystem relies on sensors like cameras, LiDARs, and RADARS to perceive the environment, localize the vehicle or robot, and plan trajectories while ensuring collision avoidance. It serves as a fundamental component for autonomous navigation.

The path planning module is responsible for generating the trajectory for the vehicle or robot to follow towards its destination. It considers objects detected by the perception system and plans to avoid collisions or getting too close to obstacles. This module utilizes a predefined map to understand constraints such as one-way roads and non-drivable areas, enabling it to plan a global path to the destination.

Lastly, the controls module issues commands to actuate and steer the vehicle or robot along the planned trajectory. Typically, separate controllers manage longitudinal and lateral movements, with one controlling throttle or brake, and the other steering the vehicle.

Below sections showcase implementations of such systems, incorporating some or all of these key components essential for autonomous navigation.

<section class="gallery-section">
<h2>Learning and perception</h2>
<div class="gallery-grid gallery-grid-three">
{% include gallery_figure.liquid path="assets/img/ROB7.gif" title="Reinforcement Learning Manipulator Control" url="https://github.com/omkarchittar/manipulator_control_DDPG" %}
{% include gallery_figure.liquid path="assets/img/SFM_square.png" title="Structure from Motion" url="https://github.com/omkarchittar/Structure_from_Motion" %}
{% include gallery_figure.liquid path="assets/img/CVDL4.png" title="LiDAR SLAM" url="https://github.com/omkarchittar/LiDAR_SLAM" %}
</div>
</section>
<section class="gallery-section">
<h2>Path planning</h2>
<div class="gallery-grid">
{% include gallery_figure.liquid path="assets/img/ROB3.png" title="Dijkstra Path Planning" url="https://github.com/omkarchittar/Dijkstra_Point_Robot" %}
{% include gallery_figure.liquid path="assets/img/ROB4.png" title="A* Path Planning" url="https://github.com/omkarchittar/A_Star_Path_Planning" %}
</div>
</section>
<section class="gallery-section">
<h2>Navigation behaviors</h2>
<div class="gallery-grid">
{% include gallery_figure.liquid path="assets/img/ROB2.png" title="Obstacle Avoiding Bot" url="https://github.com/omkarchittar/Obstacle_Avoidance_Bot" %}
{% include gallery_figure.liquid path="assets/img/ROB5.png" title="Wall Following Bot" url="https://github.com/omkarchittar/Wall_Following_Robot" %}
</div>
</section>
