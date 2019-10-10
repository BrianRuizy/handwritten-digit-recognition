<h1 align="center">
    <img alt="br logo" title="br logo" src="https://github.com/BrianRuizy/portfolio-website-3.0/blob/master/Misc/BR%20logo%20gradient.png" width="100"> </br>
     Handwritten Digit Recogntion
</h1>

<h4 align="center">
Personal portfolio python project that will be implementing a machine learning classification model to predict the value of a handwritten digit through supervised learning.
</h4>



<p align="center">
<img src="http://mdp-toolkit.sourceforge.net/_images/digits.png" >


## About
Reading letters & numbers off of a sheet of paper is profoundly intuitive for us humans, as our visual cortex has developed and evolved for thousands of years. For computers, on the other hand, interpreting strokes from a sheet of paper algorithmically is incredibly difficult. However, due to their immense processing speed, computers can take in massive amounts of data to therefore effectively *learn* and *predict* what a particular digit means. 

The model that I've opted for this particular project is the SVM model, or *linear Support Vector classification*. Although there are different approaches it is difficult to appoint a specific model as superior, as it depends on the criteria or project scope. However, SVM is the preferred method as it allows for the fine-tuning of parameters to achieve better accuracy.

## Dependencies
The algorithm itself will be given a large dataset, [MNIST](https://www.kaggle.com/c/digit-recognizer/data), from *sci-kit learn*.
Tools include:
[SciKit-learn](https://scikit-learn.org/stable/),
[matplotlib](https://matplotlib.org/)

## Versions
**Low-Level**
In the lower-level approach, you will see how a computer can read a large data set and output the users chosen element from the data structure, in a non-robust form.

![SVM3](https://user-images.githubusercontent.com/23439187/54062221-64b08500-41ca-11e9-8023-d9b4970ec05e.png)

**High-Level**
(work in progress) In the latter, higher-level, the user will be able to simply write a digit, through an input dialog, for the computer to interpret, using additional web components. 
