---
layout: page
title: 3D Vision
description: Learning for 3D Vision
img: assets/img/3D_vision_main.png
importance: 1
category: work
related_publications: true
---


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

<!-- Every project has a beautiful feature showcase page.
It's easy to include images in a flexible 3-column grid format.
Make your photos 1/3, 2/3, or full width.

To give your project a background in the portfolio page, just add the img tag to the front matter like so:

    ---
    layout: page
    title: project
    description: a project with a background image
    img: /assets/img/12.jpg
    --- -->

<div class="row">
    <div class="row justify-content-center">
        <div class="col-sm mt-3 mt-md-0"><a href="https://github.com/omkarchittar/PyTorch3D_Rendering_Basics">Renderiing Basics
            {% include figure.liquid path="assets/img/3DV1.jpg" title="Renderiing Basics" class="img-fluid rounded z-depth-1" %}</a>
        </div>
        <div class="col-sm mt-3 mt-md-0"><a href="https://github.com/omkarchittar/Single_View_to_3D">Single View to 3D
            {% include figure.liquid path="assets/img/3DV3.png" title="Single View to 3D" class="img-fluid rounded z-depth-1" %}</a>
        </div>
        <div class="col-sm mt-3 mt-md-0"><a href="https://github.com/omkarchittar/Neural_Radiance_Fields">Neural Radiance Fields
            {% include figure.liquid path="assets/img/3DV5.gif" title="Neural Radiance Fields" class="img-fluid rounded z-depth-1" %}</a>
        </div>
    </div>
</div>

<div class="caption">
    1. Learning the basics of rendering with PyTorch3D, exploring 3D representations, and practice constructing simple geometry <br>
    2. Exploring the types of loss and decoder functions for regressing to voxels, point clouds, and mesh representation from single view RGB input <br>
    3. Volume Rendering and Neural Radiance Fields <br>
</div>

<div class="container">
    <div class="row">
        <div class="col"><a href="https://github.com/omkarchittar/Neural_Surfaces">Sphere Tracing
                {% include figure.liquid path="assets/img/3DV6.gif" title="Sphere Tracing" class="img-fluid rounded z-depth-1" %}</a>
        </div>
        <div class="col"><a href="https://github.com/omkarchittar/Neural_Surfaces">Optimizing a Neural SDF
                {% include figure.liquid path="assets/img/3DV7.gif" title="Optimizing a Neural SDF" class="img-fluid rounded z-depth-1" %}</a>
        </div>
    </div>
</div>

<div class="caption">
    1. Implementing sphere tracing for rendering an SDF <br>
    2. Implementing an MLP architecture for a neural SDF, and training this neural SDF on point cloud data
</div>

<a href="https://github.com/omkarchittar/Neural_Surfaces">VolSDF</a>
<div class="container">
    <div class="row">
        <div class="col"><a href="https://github.com/omkarchittar/Neural_Surfaces">
                {% include figure.liquid path="assets/img/3DV8.gif" title="VolSDF" class="img-fluid rounded z-depth-1" %}</a>
        </div>
        <div class="col"><a href="https://github.com/omkarchittar/Neural_Surfaces">
                {% include figure.liquid path="assets/img/3DV9.gif" title="VolSDF" class="img-fluid rounded z-depth-1" %}</a>
        </div>
    </div>
</div>

<div class="caption">
    1. Implementing a function for converting SDF into volume density<br>
    2. Extending the NeuralSurface class to predict color

</div>


<a href="https://github.com/omkarchittar/Neural_Surfaces">Phong Relighting</a>
<div class="container">
    <div class="row">
        <div class="col"><a href="https://github.com/omkarchittar/Neural_Surfaces">
                {% include figure.liquid path="assets/img/3DV10.gif" title="Phong Relighting" class="img-fluid rounded z-depth-1" %}</a>
        </div>
        <div class="col"><a href="https://github.com/omkarchittar/Neural_Surfaces">
                {% include figure.liquid path="assets/img/3DV11.gif" title="Phong Relighting" class="img-fluid rounded z-depth-1" %}</a>
        </div>
    </div>
</div>

<div class="caption">
    Implementing the Phong reflection model in order to render the SDF volume we trained under different lighting conditions
</div>

<a href="https://github.com/omkarchittar/PointCloud_Classification_and_Segmentation">Point Cloud Classification</a>
<div class="container">
    <div class="row">
        <div class="col"><a href="https://github.com/omkarchittar/PointCloud_Classification_and_Segmentation">
                {% include figure.liquid path="assets/img/3DV12.gif" title="Point Cloud Classification" class="img-fluid rounded z-depth-1" %}</a>
        </div>
        <div class="col"><a href="https://github.com/omkarchittar/PointCloud_Classification_and_Segmentation">
                {% include figure.liquid path="assets/img/3DV13.gif" title="Point Cloud Classification" class="img-fluid rounded z-depth-1" %}</a>
        </div>
        <div class="col"><a href="https://github.com/omkarchittar/PointCloud_Classification_and_Segmentation">
                {% include figure.liquid path="assets/img/3DV14.gif" title="Point Cloud Classification" class="img-fluid rounded z-depth-1" %}</a>
        </div>
    </div>
</div>

<div class="caption">
    Implementing a classification model that classifies points clouds from across 3 classes (chairs, vases and lamps objects)
</div>

<a href="https://github.com/omkarchittar/PointCloud_Classification_and_Segmentation">Point Cloud Segmentation</a>
<div class="container">
    <div class="row">
        <div class="col"><a href="https://github.com/omkarchittar/PointCloud_Classification_and_Segmentation">
                {% include figure.liquid path="assets/img/3DV15.gif" title="Point Cloud Segmentation" class="img-fluid rounded z-depth-1" %}</a>
        </div>
        <div class="col"><a href="https://github.com/omkarchittar/PointCloud_Classification_and_Segmentation">
                {% include figure.liquid path="assets/img/3DV16.gif" title="Point Cloud Segmentation" class="img-fluid rounded z-depth-1" %}</a>
        </div>
        <div class="col"><a href="https://github.com/omkarchittar/PointCloud_Classification_and_Segmentation">
                {% include figure.liquid path="assets/img/3DV17.gif" title="Point Cloud Segmentation" class="img-fluid rounded z-depth-1" %}</a>
        </div>
    </div>
</div>

<div class="caption">
    Implementing a Segmentation model that segments points of chair objects into 6 semantic segmentation classes
</div>




