# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Decision Trees, Random Forests

- Unit 3: Lecture 13

  ---

  ## Materials We Provide

  | Topic  | Description            | Link                            |
  | ------ | ---------------------- | ------------------------------- |
  | Lesson | Part 1. Decision Trees | [Here](01-decision-trees.ipynb) |

  |  | Part 2. Ensembles & Random Forests | [Here](02-ensembles-random-forests_boosting.ipynb)
  | Datasets | MLB player data | [hitters.csv](./data/hitters.csv)
  | | Titanic survivors | [titanic.csv](./data/titanic.csv)
  | | Vehicles (test) | [vehicles_test.csv](./data/vehicles_test.csv)
  |  | Vehicles (train) | [vehicles_train.csv](./data/vehicles_train.csv)
  | Practice |  | [Here](./practice)

  ---

  ## Learning Objectives

  This lesson has two parts. Decision trees are introduced in part one, while random forests and other ensemble methods are elaborated on in part two. If you have limited class time, focus specifically on part one.


  ### Part One: Decision Trees

  After this lesson, students will be able to:

  - Explain how a decision tree is created
  - Build a decision tree model in scikit-learn
  - Tune a decision tree model and explain how tuning impacts the model
  - Interpret a tree diagram
  - Describe the key differences between regression and classification trees
  - Decide whether or not a decision tree is an appropriate model for a given problem

  

  ### Part Two: Ensembles & Random Forests

  After this lesson, students will be able to:

  - Define how and why decision trees can be improved using bagging and random forests
  - Build random forest models for classification and regression
  - Explain how to extract the most important predictors in a random forest model

  ---

  ## Student Requirements

  Before this lesson, students should already be able to:

  - Build and evaluate classification models in sklearn
  - Explain how and when to apply different resampling methods
  - Define the concepts of cross-validation and overfitting

  ---

  ### Lesson Outline (Part One: Decision Trees)

  - Introduction
  - A: Regression Trees
    - Group Exercise
    - Building a Regression Tree by Hand
    - How Does a Computer build a Regression Tree?
    - Demo: Choosing the Ideal Cutpoint for a Given Feature
    - Building a Regression Tree in scikit-learn
    - What Happens When We Grow a Tree Too Deep?
    - Tuning a Regression Tree
    - Making Predictions for the Testing Data
  - B: Classification Trees
    - Comparing Regression Trees and Classification Trees
    - Splitting Criteria for Classification Trees
    - Building a Classification Tree in scikit-learn
  - Summary: Comparing Decision Trees With Other Models


  ### Lesson Outline (Part Two: Ensembles & Decision Trees)

  - Introduction
  - A: Manual Ensembling
  - B: Bagging
    - Manually Implementing Bagged Decision Trees
    - Bagged Decision Trees in scikit-learn
    - Estimating Out-of-Sample Error
  - C: Random Forests
  - D: Building and Tuning Decision Trees and Random Forests
    - Optional: Predicting Salary With a Decision Tree
    - Predicting Salary With a Random Forest
    - Comparing Random Forests With Decision Trees
  - E: Tuning Individual Parameters
  - Summary

  ----

  ## Additional Resources

  *If you're interested in reading more about decision trees and random forests, check out these resources:*

  - [Induction of Decision Trees](http://hunch.net/~coms-4771/quinlan.pdf)
  - [Top 10 Algorithms in Data Mining](http://icdm.zhonghuapu.com/algorithms/10Algorithms-08.pdf)


  *If you're looking for additional references, we recommend the following books:*

  - __CHAPTER 8__ - [An Introduction to Statistical Learning](http://www-bcf.usc.edu/~gareth/ISL/) - This book provides a fantastic introduction to machine learning models and the statistics behind them. The visuals and explanations are really easy to understand. PDF available to download on the website.
  - __CHAPTER 9__ - [Elements of Statistical Learning](http://statweb.stanford.edu/~tibs/ElemStatLearn/) - This book is by most of the same authors as the previous book, but goes into more detail. PDF available to download on the website.
  - __CHAPTER 8__ - [Applied Predictive Modeling](https://www.amazon.com/Applied-Predictive-Modeling-Max-Kuhn/dp/1461468485) - While this book features R code, the discussion of different predictive models and sampling methodologies are hard to beat.