# Pathfinding-Visualisation

## Description

This project was developed using Python and the Pygame library, in order to create a visual demonstration of how two of the most popular pathfinding algorithms, Dijkstra and A*, work on a graph. The graph structure is implemented by a grid of nodes connected together, allowing for left, right, up, down and diagonal connections, meaning that the heuristic in the A* algorithm is Pythagorean rather than based on Manhattan Distance. 

## Accessing the Project

If you would like to try out the project on your own machine, please download the entire repository and ensure that you have Python 3.8 or higher and Pygame installed. Once that is done, running 
``` rb
python main.py
```
in the project directory should be enough to start the program. Once the program is started, click the node you would like your start point to be, before clicking your end goal point. Any clicking after these two points have been set will allow you to draw the barriers that the algorithm has to navigate around (be careful while doing this, leave any diagonal gaps and the path will sneak through ;)). Right clicking will allow you to reset a node to its base state if you so desire. Once you wish to run the algorithm, pressing ```1``` will run the A* Algorithm, while ```2``` will run Dijkstra's algorithm. Once the algorithm has completed, press ```C``` to clear the grid and repeat as you will!

Thank you very much for reading all this if you made it this far, I hope you enjoyed :)

## Sample Outputs for the website (matth1eumartin.github.io/matthieumartin)

![astar](https://user-images.githubusercontent.com/94123711/188642392-32cd993d-4c66-4c2b-8667-43e51ce5b01f.gif)

![dijkstra](https://user-images.githubusercontent.com/94123711/189365987-f01689d5-0634-4c28-b8c8-79539b2d6fd0.gif)
