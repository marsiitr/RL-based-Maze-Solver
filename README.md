# RL-based Maze Solver
Open Projects 2021

<p align = "center">
<img src = "https://github.com/tushdon2/RL-based-Maze-Solver/blob/main/Images%20and%20Videos/Images/Input%20maze1_animated%20solution.gif" alt = "Input Maze Animated Solution">
<br>fig1 <i>Input Maze Animated Solution</i> <br></br>
<img src = "https://github.com/tushdon2/RL-based-Maze-Solver/blob/main/Images%20and%20Videos/Images/Input%20maze1%20and%20solution.png" alt = "Input Maze Solution">
<br>fig2 <i>Input Maze Solution</i> <br></br>
<img src = "https://github.com/tushdon2/RL-based-Maze-Solver/blob/main/Images%20and%20Videos/Images/Randomly%20generated%20maze%20and%20Solution.png" alt = "Random Maze Solution">
<br>fig3 <i>Random Maze Solution</i></p>

## Abstract
<p align = "justify">The aim of this project is to solve a given 2D maze (given as an image input) using RL (Q-Learning) algorithm. The program first processes the image input of the maze and converts it into a matrix. The Q-Learning algorithm then uses this matrix to generate a q-matrix, which is finally used to get the shortest path. The program can also generate random mazes and then solve it.</p>

## Motivation
<p align = "justify">Reinforcement learning in robotics has been a challenging domain in the field of AI for the past few years. The ability to equip a robot with a powerful enough tool to allow an autonomous discovery of an optimal behavior through trial-and-error interactions with its environment has paved the path to many deep research projects.<br></br>
Our project inspires us to solve many problems, like Autonomous Mobile Robot Obstacle Prevention using Q-learning.</p>

<p align = "center">
<img src = "https://github.com/tushdon2/RL-based-Maze-Solver/blob/main/Images%20and%20Videos/Images/Input%20maze2_image%20processing.png" alt = "Image Processing">
<br>fig4 <i>Image Processing</i></p>

<!-- ## Mechanical Aspect of the Design -->

<!-- ## Electronics Aspect of the Design -->

## Software Aspect of the Design
* <p align = "justify"><b>Python</b> - It is an <b>interpreted high-level object-oriented</b> programming language designed by <b>Guido van Rossum</b>. It emphasizes code readability with significant use of indentation. It has tons of third-party open-source libraries (which can be installed using its own package manager <b><i>pip</i></b>) to assist all types of programs.</p>
* <p align = "justify"><b>Jupyter Notebook</b> - It is a product developed under <b><i>Project Jupyter</i></b> (spun off from <b><i>IPython</i></b> in 2014 by <b>Fernando Perez</b>) and is used to create documents containing live code, equations, visualizations and narrative text. It is used in data cleaning and transformation, numerical simulation, statistical modeling, data visualization, machine learning, etc.</p>
* <p align = "justify"><b>NumPy</b> - It is a Python library providing fundamental package for scientific computing. It is used for working with arrays in the domain of linear algebra, fourier transform, matrices, etc. Numpy arrays are 50x faster than Python lists.</p>
* <p align = "justify"><b>Matplotlib</b> - It is a Python library for creating static, animated, and interactive visualizations and plots and was introduced by <b>John D. Hunter</b> in 2002.</p>
* <p align = "justify"><b>Python Imaging Library (PIL)</b> - It is a Python library providing support for opening, manipulating, and saving many different image file formats. It supports Python version 1.5.2 to 2.7. A subsequent fork of the PIL repository named <b><i>Pillow</i></b> added Python 3.x support.</p>


## Cost Structure
| Software (Components) | Cost |
|:---------------------:|:----:|
| Python | Open-Source/None |
| Jupyter Notebook | Open-Source/None |
| NumPy | Open-Source/None |
| Matplotlib | Open-Source/None |
| PIL | Open-Source/None |

## Applications
<p align = "justify">This project can be used to develop a navigation system with the ability to learn to adapt to unknown environments. Such game-playing AIs are designed in a way that  their solutions are relevant in many practical applications :</p>

* <p align = "justify"><b>Industrial Applications</b> - Mobile robots have been increasingly used  over the last two decades in various industries to move goods from one place to another with optimal movement policy.</p>
* <p align = "justify"><b>Restaurants of the Future (ROTF)</b> - ROTF is one of the greatest physical application of the project. Since such a RL based implementation in a mobile robot will help us to give and take orders from the customers, in a faster and more efficient way.</p>
* <p align = "justify"><b>Navigation</b> - Maze solving can further be extended for autonomous navigation in an occupancy grid to get to the nearest landmark like an EV charging station or a petrol pump.</p>

## Limitations
At the current state, our project has a few limitations :
* <p align = "justify">Before running, the program requires <b><i>total number of episodes</i></b> and <b><i>number of random episodes</i></b> to be given as a manual input. These can be developed as a function of the maze size to get a higher degree of automation.</p>
* The [`reduceMatrix()`](https://github.com/tushdon2/RL-based-Maze-Solver/blob/fbd11ce17a93b9e0d79abbe9c3acc61b46c69b3a/src/ImgPreprocess.py#L49), [`trim()`](https://github.com/tushdon2/RL-based-Maze-Solver/blob/fbd11ce17a93b9e0d79abbe9c3acc61b46c69b3a/src/ImgPreprocess.py#L137) and [`sharpen()`](https://github.com/tushdon2/RL-based-Maze-Solver/blob/fbd11ce17a93b9e0d79abbe9c3acc61b46c69b3a/src/ImgPreprocess.py#L193) functions also require manual passing of parameters.
* <p align = "justify">The <b><i>Image Processing</i></b> part of our project is not strong enough to process very low-resolution maze images.</p>
* <p align = "justify">The simple reinforcement learning algorithm would collapse when dealing with complex mazes.</p>


## Future Improvements
In future, we plan to :
* <p align = "justify">generate an animated maze solution. </p>
* <p align = "justify">implement <b><i>Multi-Objective target search</i></b>, wherein the agent of Q-Learning must visit intermediate <b><i>flag</i></b> positions before going to the end of the maze.</p>
* <p align = "justify">extend our project to 3-D Mazes.</p>

## Team Members
* [Apurba Prasad Padhy](https://github.com/apurba-pp)
* [Chirag Arora](https://github.com/chirag-ar)
* [Rishabh Dubey](https://github.com/RishabhDubey03)
* [Tushar Sahu](https://github.com/tushdon2)
* [Yash Bhinwal](https://github.com/yash-bhinwal)

## Mentors
* [Agrim Agrawal](https://github.com/Agrim01)
* [Annu Shree](https://github.com/annushree21)
* [Vansh Goyal](https://github.com/vanshgoyal)


## References
* Python :
  * [Youtube/freeCodeCamp.org](https://www.youtube.com/watch?v=rfscVS0vtbw)
  * [Programiz](https://www.programiz.com/python-programming)
  * [W3Schools](https://www.w3schools.com/python/)
* Graph Theory :
  * [Progamiz](https://www.programiz.com/dsa/graph)
  * [Youtube/freeCodeCamp.org](https://www.youtube.com/watch?v=09_LlHjoEiY)
* Dijkstra Algorithm :
  * [Programiz](https://www.programiz.com/dsa/dijkstra-algorithm)
  * [Youtube/Abdul Bari](https://www.youtube.com/watch?v=XB4MIexjvY0)
  * [Brilliant](https://brilliant.org/wiki/dijkstras-short-path-finder/)
* Bellman Ford's Algorithm :
  * [Programiz](https://www.programiz.com/dsa/bellman-ford-algorithm)
  * [Youtube/Abdul Bari](https://www.youtube.com/watch?v=FtN3BYH2Zes)
* Reinforcement Learning :
  * [Youtube/DeepMind](https://www.youtube.com/playlist?list=PLqYmG7hTraZDM-OYHWgPebj2MfCFzFObQ)
  * [samyzaf.com](https://www.samyzaf.com/ML/rl/qmaze.html)
* Q-Learning :
  * [Youtube/deeplizard](https://www.youtube.com/watch?v=qhRNvCVVJaA)
  * [Wikipedia](https://en.m.wikipedia.org/wiki/Q-learning)
* Matplotlib:
  * [GeeksforGeeks](https://www.geeksforgeeks.org/matplotlib-pyplot-imshow-in-python/)
* Image Processing of the Maze : 
  * [stackoverflow](https://stackoverflow.com/questions/57610416/how-to-read-a-maze-from-an-image-and-convert-it-to-binary-values-in-python)
