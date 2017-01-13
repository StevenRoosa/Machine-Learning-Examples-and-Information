# Background
These are a few simple examples of machine learning in Python.  Adding more soon, so stay tuned.
To get started, I recommend using Jupyter Notebook and Anaconda as part of your environnment. <a href="http://jupyter.org/install.html">This is the place to go to get quickly started with Jupyter and Anaconda</a>. Licensing info at the bottom of the document.

# Monty Hall - Bayesian Inference
I put together a [simulation](StevenRoosa/Machine-Learning-Examples-and-Information/monty_hall.ipynb) of the Monty Hall paradox. It is an example of Bayesian belief at work.
There is a great write up of the Monty Hall paradox on <a href="https://en.wikipedia.org/wiki/Monty_Hall_problem">wikipedia</a>.

# Neural Networks - TensorFlow
To get started on TensorFlow, the <a href="https://www.tensorflow.org/get_started/os_setup">documentation</a> is excellent.
The TensorFlow file in this repo is an example using Google's machine learning platform,
specifically the neural network functionality.  The dataset comes from the classic breast
biopsy dataset <a href="https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data">made available here</a>.  Prior to splitting the dataset into training and test files, a few adjustments to the dataset are necessary. You can use a couple of handy   
sed commands in the Bash terminal or just use Jupyter Notebook.
  
First, a command to remove all lines with missing data, i.e. lines containing "?":  
Bash: $sed -i '/?/d' datafile.txt  
Jupyter: !$sed -i '/?/d' datafile.txt

Second, a command to remove index numbers:  
Bash: $sed -i 's/^[^,]*,//' datafile.txt  
Jupyter: !$sed -i 's/^[^,]*,//' datafile.txt 

Third, commands to change target variable values for malignant (4) and benign (2) to 1 and 0, respectively:  
Bash: $sed -i 's/4$/1/' datafile.txt  
Jupyter: !$sed -i 's/2$/0/' datafile.txt  

Finally, you will need to split the datset into training and test datasets. To do this, you can, after making the noted modifications with sed, open up the [TensorFlow workbench file in this repo](StevenRoosa/Machine-Learning-Examples-and-Information/tensor_workbench.ipynb) and select your dataset.  Then walk through the boxes and execute them as described in the notebook.    
  
# K-Nearest Neighbor is Coming Soon...
Adding K-Nearest Neighbor next ....

# Python Machine Learning Book Recommendation
For a great book on Machine Learning with Python, try <a href="https://www.amazon.com/Python-Machine-Learning-Sebastian-Raschka/dp/1783555130/">Python Machine Learning</a> by Sebastian Raschka.

# Accountable Algorithms - Work of Dr. Josh Kroll et al.
For social implications and thoughts on accountability, 
please see the work of Dr. Josh Kroll, PhD., in particular his work on 
[Accountable Algorithms](StevenRoosa/Machine-Learning-Examples-and-Information/SSRN-id2765268 (2).pdf) which is published in University of Pennsylvania Law Review, Vol. 165, 2017. 

# Copyright and License Info:
The copyright on the content in this repo, unless otherwise noted, is owned by Steven Roosa, but you are welcome to use it on an AS IS basis, with no warranties, and to have a worldwide, irrevocable, non-exclusive license.
