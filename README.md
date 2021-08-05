# RL-based Maze Solver
Open Projects 2021

![Input Maze Solution](https://github.com/tushdon2/RL-based-Maze-Solver/blob/main/Images%20and%20Videos/Images/Input%20maze1%20and%20solution.png)

![Random Maze Solution](https://github.com/tushdon2/RL-based-Maze-Solver/blob/main/Images%20and%20Videos/Images/Randomly%20generated%20maze%20and%20Solution.png)

## Abstract
<p align = "justify">The aim of this project is to solve a given 2D maze (given as an image input) using RL (Q-Learning) algorithm. The program first processes the image input of the maze and converts it into a matrix. The Q-Learning algorithm then uses this matrix to generate a q-matrix, which is finally used to get the shortest path. The program can also generate random mazes and then solve it.</p>

## Motivation
<p align = "justify">Reinforcement learning in robotics has been a challenging domain in the field of AI for the past few years. The ability to equip a robot with a powerful enough tool to allow an autonomous discovery of an optimal behavior through trial-and-error interactions with its environment has paved the path to many deep research projects.<br></br>
Our project inspires us to solve many problems, like Autonomous Mobile Robot Obstacle Prevention using Q-learning.</p>

![Image Processing](https://github.com/tushdon2/RL-based-Maze-Solver/blob/main/Images%20and%20Videos/Images/Input%20maze2_image%20processing.png)

<!-- ## Mechanical Aspect of the Design -->

<!-- ## Electronics Aspect of the Design -->

## Cost Structure
| Software (Components) | Cost |
|:---------------------:|:----:|
| Python | Open-Source/None |
| Jupyter Notebook | Open-Source/None |
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
