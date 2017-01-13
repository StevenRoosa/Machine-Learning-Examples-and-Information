# Background
These are a few simple examples of machine learning in Python.
It has been put together on an expedited basis, so apologies in advance for any snafus.
I have added Jupyter Notebook versions first, but will try and augment with 
flat Python script files in the future. 

# Jupyter Notebook
To get started with Jupyter Notebook, using Anaconda is the easiest, 
and <a href="http://jupyter.org/install.html">this is the place to go</a>.

# Monty Hall - Bayesian Inference
The Monty Hall file in this repo is a simulation of the paradox of the same name, 
and is an example of Bayesian belief at work.
There is a great write up of the Monty Hall paradox on <a href="https://en.wikipedia.org/wiki/Monty_Hall_problem">wikipedia</a>.

# Neural Networks - TensorFlow
The TensorFlow file in this repo is an example using Google's machine learning platform,
specifically the neural network functionality.  The dataset comes from the classic breast
biopsy dataset <a href="https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data">made available here</a>.  Prior to splitting the dataset into training and test  
files, first a few adjustments to the dataset are in order. You can use a couple of handy   
sed commands in the bash terminal.  
First, a command to remove all lines missing data, i.e. lines containing "?":  
$sed -i '/?/d' datafile.txt  
Second, a command to remove entry ID numbers:  
$sed -i 's/^[^,]*,//' datafile.txt  
Third, commands to change target variable values for malignant (4) and benign (2) to 1 and 0, respectively:  
$sed -i 's/4$/1/' datafile.txt  
$sed -i 's/2$/0/' datafile.txt  
To get started on TensorFlow, the <a href="https://www.tensorflow.org/get_started/os_setup">documentation</a> is really good.  

# K-Nearest Neighbor is Coming Soon...
Adding K-Nearest Neighbor next ....

# Python Machine Learning Book Recommendation
For a great book on Machine Learning with Python, try <a href="https://www.amazon.com/Python-Machine-Learning-Sebastian-Raschka/dp/1783555130/">Python Machine Learning</a> by Sebastian Raschka.

# Accountable Algorithms - Work of Dr. Josh Kroll et al.
For social implications and thoughts on accountability, 
please see the work of Dr. Josh Kroll, PhD., in particular his work on 
[Accountable Algorithms](StevenRoosa/Machine-Learning-Examples-and-Information/SSRN-id2765268 (2).pdf) which is published in University of Pennsylvania Law Review, Vol. 165, 2017. 
