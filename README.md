# Warehouse-Stock-Level-Prediction-App


<p> <b>Data@ANZ</b> is about mining and linking datasets to develop stories that matter and challenge the status quo, to deliver on ANZ’s purpose `to shape a world where people and communities thrive`. This virtual internship seeks to equip young professionals with data analytics and predictive modeling skills that can be implemented in most organizations.

Further details about the program can be assessed [here](https://www.theforage.com/virtual-internships/prototype/ZLJCsrpkHo9pZBJNY/ANZ-Virtual-Internship?ref=tCfFoXSNJ4aLnBQye)</p> 
- The program consists of 2 modules.
- The files in this repository are only my submitted files.

<br>

## Table of Contents
* [Installing Packages](#ip)
* [Project Motivation](#pm)
* [File Description](#fd)
* [Methodology](#md)
* [Results](#re)
* [Certificate](#cf)


<br>

## Installing Packages<a name="ip"></a>
<p style='text-align:justify;'>To run the jupyter notebook on your localhost, I recommend you install the packages I used for this project. You can do that by;</p>

1. Download the requirements.txt file and save it into the directory you'll be working from.
2. Create a conda environment with python 3.*

	```python

	conda create --name env-name python==3.7
	```
3. Now install the packages from the requirements.txt file. Make sure you're in folder that has the file.

	```python

	pip install requirements.txt
	```
4. Finally, activate the environment and run the downloaded jupyter notebook

	```python

	conda activate env-name
	```
<br>

## Project Motivation<a name="pm"></a>
<details>
	<summary>Problem Statement</summary>
	<br>
	<p style='text-align:justify;'>ANZ has a synthesised transaction dataset containing 3 months’ worth of transactions for 100 hypothetical customers. It contains purchases, recurring transactions, and salary transactions. Based on this dataset, ANZ will want to understand the behaviours of their customers and how transactions are undertaken by each hypothetical customer and finally, be able to predict the annual salary of their present and potential customers.</p>

</details>

<details>
	<summary>Project Goals</summary>
	<br>
	<p>In this project, I wanted to achieve 2 main goals and they are;</p>
	<ol>
		<li>Segment dataset and draw unique insights, including visualization of the transaction volume and assessing the effect of any outliers.</li>
		<li>Explore correlation between customer attributes and build a regression and a decision-tree prediction model based on your findings.</li>
	</ol>
</details>

<br>

## File Description <a name="fd"></a>
This repository contains one Jupyter notebook that has all the code for data cleansing, EDA and machine learning. There is also a python script that contains code for the deployment of ml model. Finally, there is a pickle file which is the trained model.

<br>

## Methodology<a name="md"></a>
<details>
	<summary>Data Quality Assessment</summary>
	<br>
	<p style='text-align:justify;'>The first task that I performed under the data preparation step was initial assessment of the quality of data which easily allowed me to properly clean the data. The following were some of the issues discovered;</p>
	<ul>
		<li>Missing values in some of the columns with 2 of those columns having missing values above 40%.</li>
		<li>Discovered some columns will not be needed for the analysis.</li>
		<li>Some of the data types were not properly formatted including the date.</li>
		<li>Spatial coordinates needed to be separated.</li>
	</ul>
</details>

<details>
	<summary>Data Cleaning and Preprocessing</summary>
	<br>
	<p style='text-align:justify;'>In the preprocessing step (usually an iterative process) I cleaned the data based on data quality issues identified. Some of           the task I performed in this step include;</p>
	<ul>
		<li>Handling missing values</li>
		<li>Dropping unneeded columns</li>
		<li>Proper date formatting</li>
		<li>Splitting of spatial data(longitude and latitude column)</li>
	</ul>
</details>

<details>
<summary>Exploratory Data Analysis</summary>
<br>
One of the goals for this project as mentioned earlier was to segment dataset and draw unique insights, including visualization of the transaction volume and assessing the effect of any outliers. Based on this stated goal, I performed any set of anylysis on the cleaned data to obtain insights that helped me to arrive at some plausible conclusions. 

<p>&nbsp;</p>
	
To achieve the first goal, I answered a few questions using both quantitative and graphical methods. Some of the questions are listed below.
	
* Are males performing more transactions as compared to females?
* What is the average spending by the customers?
* Are most of the transactions authorized?
* Between males and females, who spends a lot?
* Which suburb do most of the transactions take place?
* How does spending vary with state?
* How did the average amount spent by customers changed over time ( days, weeks)?	
</details>


<details>
<summary>Statistical Analysis</summary>
<br>
For this task I further looked into the question that was asked about the spending habit of customers based on their gender. I found out that the number of male customers performed a lot of debit transactions than their female counterparts. I therefore needed to clearly conclude without any doubt that males spend more than females and that the difference is not due to chance. To do this I performed hypothesis testing(Welch's t-Test) to draw conclusion on the result.
</details>

<details>
<summary>Feature Selection and Engineering</summary>
<br>
The better I prapare the data for modeling, the better my model will perform. In this task, I properly prepared my data by transforming columns, dropping irrelevant columns, handling missing and categorical values and finally engineering new features. Some of the tasks I performed for this step include;	
	
* Creating and merging new features(annual salary, annual spending and spending ratio)
* Grouped age of customers into bins as well as spending ration
* Computed salary payment freuqency and monthly average salary
* Dropped highly correlated features	
</details>

<details>
<summary>Predictive Modeling</summary>
<br>
To complete this task I went through the various machine learning steps which includes;
	
* Data Loading - In this task I loaded the cleaned data that contained all the engineered features as well as the selected ones.
* Data Understanding - In this step, I used both graphical and quantitative methods to explore the distributions and correlations between customer                attributes.
* Data Splitting - I then went ahead and split the data into train and test data in readiness for modeling.
* Algorithm Evaluation - In this step, I trained various algorithms on a standardized dataset using default parameters and 12-fold cross-validation. 
* Parameter Tuning - The best model turned out to be Ridge Regressor which I later went ahead to tune its parameters for better performance using                   Grid Search.
* Final Model - At this stage, the model was ready to make predictions. The model was able to predict the annual salaries of customers with RMSE of                  8660 and R-score of approximately 90%. 
* Model Understanding -  I wanted to know how the trained model performed and what were the main drivers. I plotted the difference between the y-test and predictions and had a linear relationship which means the model did a good job at predicting the annual salaries.
</details>

<br>

## Results<a name="re"></a>
Based on the analysis I performed, below are the key insights I generated from the data; 

* There were more authorized transactions, approximately 7600 in total as compared to posted transactions which was approximately 5000 in total. Having a lot of authorized transactions can increase customer frustration since they wull have to wait for some days before their transactions are completed. To ensure good customer services, it will be important to probe this transactions and find out where the blockers are.
* Most of the transactions were performed by male customers as compared to females and the same reflects in the amount transacted as well. 
* I was able to conclude that male customers were the bigger spenders with an average of 55 AUD as compared to 50 AUD for females. Also, based on the dataset I was 95% confident that male customers will spend between 28.2 AUD and 29.2 AUD on average and female customers will spend between 26.4 AUD and 27.4 AUD on average.
* Sydney and Melbourne were the suburbs that saw a lot of transactions occuring. Which means that services such as ATM must run efficiently to meet customer demands.
 
<br>

## Certificate<a name="cf"></a> 
[Earned Certificate](https://insidesherpa.s3.amazonaws.com/completion-certificates/ANZ/ZLJCsrpkHo9pZBJNY_ANZ_tCfFoXSNJ4aLnBQye_completion_certificate.pdf)
