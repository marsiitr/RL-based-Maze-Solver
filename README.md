# RL-based Maze Solver
Open Projects 2021

![Input Maze Solution](https://github.com/tushdon2/RL-based-Maze-Solver/blob/main/Images%20and%20Videos/Images/Input%20maze1%20and%20solution.png)
<br>fig1 <i>Input Maze Solution</i>

![Random Maze Solution](https://github.com/tushdon2/RL-based-Maze-Solver/blob/main/Images%20and%20Videos/Images/Randomly%20generated%20maze%20and%20Solution.png)
<br>fig2 <i>Random Maze Solution</i>

## Abstract
<p align = "justify">The aim of this project is to solve a given 2D maze (given as an image input) using RL (Q-Learning) algorithm. The program first processes the image input of the maze and converts it into a matrix. The Q-Learning algorithm then uses this matrix to generate a q-matrix, which is finally used to get the shortest path. The program can also generate random mazes and then solve it.</p>

## Motivation
<p align = "justify">Reinforcement learning in robotics has been a challenging domain in the field of AI for the past few years. The ability to equip a robot with a powerful enough tool to allow an autonomous discovery of an optimal behavior through trial-and-error interactions with its environment has paved the path to many deep research projects.<br></br>
Our project inspires us to solve many problems, like Autonomous Mobile Robot Obstacle Prevention using Q-learning.</p>

![Image Processing](https://github.com/tushdon2/RL-based-Maze-Solver/blob/main/Images%20and%20Videos/Images/Input%20maze2_image%20processing.png)
<br>fig3 <i>Image Processing</i>

<!-- ## Mechanical Aspect of the Design -->

<!-- ## Electronics Aspect of the Design -->

## Software Aspect of the Design
* **Python** - It is an **interpreted high-level object-oriented** programming language designed by **Guido van Rossum**. It emphasizes code readability with significant use of indentation. It has tons of third-party open-source libraries (which can be installed using its own package manager **_pip_**) to assist all types of programs. 
* **Jupyter Notebook** - It is a product developed under **_Project Jupyter_** (spun off from **_IPython_** in 2014 by **Fernando Perez**) and is used to create documents containing live code, equations, visualizations and narrative text. It is used in data cleaning and transformation, numerical simulation, statistical modeling, data visualization, machine learning, etc.
* **NumPy** - It is a Python library providing fundamental package for scientific computing. It is used for working with arrays in the domain of linear algebra, fourier transform, matrices, etc. Numpy arrays are 50x faster than Python lists.
* **Matplotlib** - It is a Python library for creating static, animated, and interactive visualizations and plots and was introduced by **John D. Hunter** in 2002.
* **Python Imaging Library (PIL)** - It is a Python library providing support for opening, manipulating, and saving many different image file formats. It supports Python version 1.5.2 to 2.7. A subsequent fork of the PIL repository named **_Pillow_** added Python 3.x support.

## Cost Structure
| Software (Components) | Cost |
|:---------------------:|:----:|
| Python | Open-Source/None |
| Jupyter Notebook | Open-Source/None |
| NumPy | Open-Source/None |
| Matplotlib | Open-Source/None |
| PIL | Open-Source/None |

## Applications
This project can be used to develop a navigation system with the ability to learn to adapt to unknown environments. Such game-playing AIs are designed in a way that  their solutions are relevant in many practical applications :  
* **Industrial Applications** - Mobile robots have been increasingly used  over the last two decades in various industries to move goods from one place to another with optimal movement policy.
* **Restaurants of the Future (ROTF)** -  ROTF is one of the greatest physical application of the project. Since such a RL based implementation in a mobile robot will help us to give and take orders from the customers, in a faster and more efficient way. 
* **Navigation** - Maze solving can further be extended for autonomous navigation in an occupancy grid to get to the nearest landmark like an EV charging station or a petrol pump.

## Limitations
At the current state, our project has a few limitations :
* Before running, the program requires **_total number of episodes_** and **_number of random episodes_** to be given as a manual input. These can be developed as a function of the maze size to get a higher degree of automation.
* The [`reduceMatrix()`](https://github.com/tushdon2/RL-based-Maze-Solver/blob/fbd11ce17a93b9e0d79abbe9c3acc61b46c69b3a/src/ImgPreprocess.py#L49), [`trim()`](https://github.com/tushdon2/RL-based-Maze-Solver/blob/fbd11ce17a93b9e0d79abbe9c3acc61b46c69b3a/src/ImgPreprocess.py#L137) and [`sharpen()`](https://github.com/tushdon2/RL-based-Maze-Solver/blob/fbd11ce17a93b9e0d79abbe9c3acc61b46c69b3a/src/ImgPreprocess.py#L193) functions also require manual passing of parameters.
* The _**Image Processing**_ part of our project is not strong enough to process very low-resolution maze images. 
* The simple reinforcement learning algorithm would collapse when dealing with complex mazes. 


## Future Improvements
In future, we plan to :
* generate an animated maze solution. 
* implement **_Multi-Objective target search_**, wherein the agent of Q-Learning must visit intermediate **_flag_** positions before going to the end of the maze.
* extend our project to 3-D Mazes.

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
