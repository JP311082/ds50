# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Experiments and Hypothesis Testing

> Unit 2, Session 8

---

## Materials We Provide

| Topic | Description | Link |
| --- | --- | --- |
| Lesson | Experiments and Hypothesis Testing Lesson | [Here](01-data-experiments-causation.ipynb) |
|                 |                                                              |                                             |
| Practice | Individual Practice Activity (includes data and sample solutions) | [Here](practice/) |
|  |  |  |
| Extra Materials | French Fry Study | [Here](./assets/french-fry.pdf) |

> In this lesson, we'll use an online CSV file about advertising data, taken from the book "An Introduction to Statistical Learning". This dataset is easy to understand. It allows you to easily compare sales data across three advertising mediums.

---

## Learning Objectives

By the end of this lesson, students will be able to:
- Explain the difference between causation and correlation
- Determine causality and sampling bias using Directed Acyclic Graphs
- Identify what missing data is and how to handle it
- Test a hypothesis using a sample case study

---

## Student Requirements

Before this lesson(s), students should already be able to:
- Perform basic data analysis in Pandas
- Have a basic understanding of bias, variance, and correlation
- Create basic visualizations in Seaborn
- Have some exposure to major considerations within experimental design

----

## Lesson Outline


- Data Source
	- What are the features/covariates/predictors?
	- What is the outcome/response?
	- What do you think each row in the dataset represents?
- Causation and Correlation
	- Structure of causal claims
	- Why do we care?
	- How do we determine if something is causal?
- Sampling bias
	- Forms of sampling bias
	- Problems from sampling bias
	- Recovering from sampling bias
    	- Stratified random sampling
- Missing data
	- Types of missing data
	- De minimis
	- Class imbalance
    	- Relation to machine learning
- Introduction to Hypothesis Testing
	- Validate your findings
	- Confidence intervals
	- Error types
- Scenario
	- Exercises
	- Statistical Tests
	- Interpret your results

---

## Additional Resources

For more information on this topic, check out the following resources:
- [An Introduction to Statistical Learning](http://www-bcf.usc.edu/~gareth/ISL/)
- [The more advanced book: Elements of Statistical Learning](http://web.stanford.edu/~hastie/ElemStatLearn/)
- [Spurious Correlations](http://www.tylervigen.com/spurious-correlations)
- Wikipedia pages on [ANOVA](https://en.wikipedia.org/wiki/Analysis_of_variance), [Welch's t-test](https://en.wikipedia.org/wiki/Welch's_t-test), [Mann-Whitney test](https://en.wikipedia.org/wiki/Mann%E2%80%93Whitney_U_test)
