---
layout: page
title: 3D Computer Vision
description: Learning for 3D Vision
img: assets/img/3DV0.png
importance: 2
category: earlier-work
project_gallery: true
---

{% include gallery_figure.liquid path="assets/img/3D_vision_main.png" title="Learning-based 3D vision overview" caption="An overview of learning-based 3D vision." overview=true %}

Developing autonomous agents requires them to understand and interact within a 3D environment. The capability to deduce, shape, and apply 3D representations is crucial in AI for various applications, including robotic handling, autonomous driving, virtual reality, and photo editing. The ambition to comprehend 3D spaces in computer vision has made significant strides with the advent of advanced (deep) learning methods. This area aims to delve into the integration of 3D Vision with Learning-based approaches, highlighting recent breakthroughs in the field.

It covers topics including:

- Explicit, Implicit, and Neural 3D Representations
- Differentiable Rendering
- Single-view 3D Prediction: Objects, Scenes, and Humans
- Neural Rendering
- Multi-view 3D Inference: Radiance Fields, Multi-plane Images, Implicit Surfaces, etc.
- Generative 3D Models
- Shape Abstraction
- Mesh and Point cloud processing

<section class="gallery-section">
<h2>Rendering and reconstruction</h2>
<div class="gallery-grid gallery-grid-three">
{% include gallery_figure.liquid path="assets/img/3DV1.jpg" title="Rendering Basics" url="https://github.com/omkarchittar/PyTorch3D_Rendering_Basics" caption="Explore 3D representations and construct simple geometry with PyTorch3D." %}
{% include gallery_figure.liquid path="assets/img/3DV3.png" title="Single View to 3D" url="https://github.com/omkarchittar/Single_View_to_3D" caption="Explore losses and decoders for voxels, point clouds, and meshes from a single RGB image." %}
{% include gallery_figure.liquid path="assets/img/3DV5.gif" title="Neural Radiance Fields" url="https://github.com/omkarchittar/Neural_Radiance_Fields" caption="Volume rendering and neural radiance fields." %}
</div>
</section>
<section class="gallery-section">
<h2>Neural surfaces</h2>
<div class="gallery-grid">
{% include gallery_figure.liquid path="assets/img/3DV6.gif" title="Sphere Tracing" url="https://github.com/omkarchittar/Neural_Surfaces" caption="Implement sphere tracing to render a signed distance field." %}
{% include gallery_figure.liquid path="assets/img/3DV7.gif" title="Optimizing a Neural SDF" url="https://github.com/omkarchittar/Neural_Surfaces" caption="Train an MLP-based neural signed distance field on point cloud data." %}
</div>
</section>
<section class="gallery-section">
<h2>VolSDF</h2>
<div class="gallery-grid">
{% include gallery_figure.liquid path="assets/img/3DV8.gif" title="Volume density" url="https://github.com/omkarchittar/Neural_Surfaces" caption="Convert a signed distance field into volume density." %}
{% include gallery_figure.liquid path="assets/img/3DV9.gif" title="Color prediction" url="https://github.com/omkarchittar/Neural_Surfaces" caption="Extend the neural surface to predict color." %}
</div>
</section>
<section class="gallery-section">
<h2>Phong Relighting</h2>
<p>Render the trained SDF volume under different lighting conditions using the Phong reflection model.</p>
<div class="gallery-grid">
{% include gallery_figure.liquid path="assets/img/3DV10.gif" title="Relighting example 1" url="https://github.com/omkarchittar/Neural_Surfaces" %}
{% include gallery_figure.liquid path="assets/img/3DV11.gif" title="Relighting example 2" url="https://github.com/omkarchittar/Neural_Surfaces" %}
</div>
</section>
<section class="gallery-section">
<h2>Point Cloud Classification</h2>
<p>Classify point clouds across three classes: chairs, vases, and lamps.</p>
<div class="gallery-grid gallery-grid-three">
{% include gallery_figure.liquid path="assets/img/3DV12.gif" title="Classification example 1" url="https://github.com/omkarchittar/PointCloud_Classification_and_Segmentation" %}
{% include gallery_figure.liquid path="assets/img/3DV13.gif" title="Classification example 2" url="https://github.com/omkarchittar/PointCloud_Classification_and_Segmentation" %}
{% include gallery_figure.liquid path="assets/img/3DV14.gif" title="Classification example 3" url="https://github.com/omkarchittar/PointCloud_Classification_and_Segmentation" %}
</div>
</section>
<section class="gallery-section">
<h2>Point Cloud Segmentation</h2>
<p>Segment chair point clouds into six semantic classes.</p>
<div class="gallery-grid gallery-grid-three">
{% include gallery_figure.liquid path="assets/img/3DV15.gif" title="Segmentation example 1" url="https://github.com/omkarchittar/PointCloud_Classification_and_Segmentation" %}
{% include gallery_figure.liquid path="assets/img/3DV16.gif" title="Segmentation example 2" url="https://github.com/omkarchittar/PointCloud_Classification_and_Segmentation" %}
{% include gallery_figure.liquid path="assets/img/3DV17.gif" title="Segmentation example 3" url="https://github.com/omkarchittar/PointCloud_Classification_and_Segmentation" %}
</div>
</section>
<section class="gallery-section">
<h2>Multi-view geometry</h2>
<div class="gallery-grid">
{% include gallery_figure.liquid path="assets/img/3DV18.jpeg" title="Structure from Motion" url="https://github.com/omkarchittar/Structure_from_Motion" %}
</div>
</section>

## Further reading

[MVS](https://github.com/walsvid/Awesome-MVS?tab=readme-ov-file#early) · [SLAM resources](https://github.com/kanster/awesome-slam) · [More SLAM resources](https://github.com/SilenceOverflow/Awesome-SLAM)
