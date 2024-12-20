Implement DFS, BFS and UCS for the pacman game and compare the performance for tinyMaze,  mediumMaze, bigMaze.Also find the time comparisons (in miliseconds) of BFS,DFS,UCS.

How to run

# DFS on tinyMaze
python pacman.py -l tinyMaze -p SearchAgent -a fn=dfs

# DFS on mediumMaze
python pacman.py -l mediumMaze -p SearchAgent -a fn=dfs

# DFS on bigMaze
python pacman.py -l bigMaze -p SearchAgent -a fn=dfs -z .5

# BFS on tinyMaze
python pacman.py -l tinyMaze -p SearchAgent -a fn=bfs

# BFS on mediumMaze
python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs

# BFS on bigMaze
python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5

# UCS on tinyMaze
python pacman.py -l tinyMaze -p SearchAgent -a fn=ucs

# UCS on mediumMaze
python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs

# UCS on bigMaze
python pacman.py -l bigMaze -p SearchAgent -a fn=ucs -z .5
