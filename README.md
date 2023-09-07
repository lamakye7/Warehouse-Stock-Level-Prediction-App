# Warehouse-Stock-Level-Prediction-App


<p> <b>Cognizant</b> Cognizant operationalizes AI to reliably deliver efficiency, innovation and agility. The virtual internship seeks to equip young professionals Artificial Intelligence(AI) skills.
	
More details about the program can be assessed [here](https://www.theforage.com/virtual-experience/5N2ygyhzMWjKQmgCK/cognizant/cognizant-artificial-intelligence-virtual-experience-program/model-building-and-interpretation)</p> 
- The program consists of 5 tasks
  

<br>

## Table of Contents
* [Business Problem](#bp)
* [File Description](#fd)
* [Methodology](#md)
* [Results](#re)
* [Certificate](#cf)




## Business Problem<a name="bp"></a>
<details>
	<summary>Problem Statement</summary>
	<br>
	<p style='text-align:justify;'>Gala Groceries is a technology-led grocery store chain based in the USA. Gala Groceries approched Cognizant to help them solve supply chain issue. Groceries are highly perishable items, if you overstock, you are wasting money on excessive storage and waste, but if you understock, then you are losing customers. Gala Groceries want to understand sale pattern and finally able to predict the stock levels of products, on an hourly basis in order to more intelligently procure products from their suppliers.</p>

</details>

<details>
	<summary>Project Goals</summary>
	<br>
	<ol>
		<li>Draw unique insights from sale pattern, through Exploration Data Analysis .</li>
		<li>Build a predictive model to predict the hourly stock level.</li>
	</ol>
</details>

<br>

## File Description <a name="fd"></a>
This repository contains one Jupyter notebook that has all the code for data cleansing, EDA and machine learning. There is also a python script that contains code for the deployment of ml model. Finally, there is a pickle file which is the trained model.

<br>

## Methodology<a name="md"></a>

<details>
	<summary>Data Cleaning and Preprocessing</summary>
	<br>
	<p style='text-align:justify;'>In the preprocessing step (usually an iterative process) I cleaned the data based on data quality issues identified. Some of           the task I performed in this step include;</p>
	<ul>
		<li>Merging datasets</li>
		<li>Dropping unneeded columns</li>
		<li>Proper date formatting</li>
		<li>Handling missing values</li>
		<li>Removing outliiers</li>
	</ul>
</details>

<details>
<summary>Exploratory Data Analysis</summary>
<br>
One of the goals for this project as mentioned earlier was to segment dataset and draw unique insights, including visualization of the transaction volume and assessing the effect of any outliers. Based on this stated goal, I performed any set of anylysis on the cleaned data to obtain insights that helped me to arrive at some plausible conclusions. 

<p>&nbsp;</p>
	
I provided answer to the following questions to draw insight from the dataset

* What is the distribution of the numerical dtype?
* What is the distribution of the categorical columns?
* How does the trend for stock level and total sale differ per hour?
* What is the total quantity sold per category?
* What is the total sales per category?
* What is the average sale per product category?
* What is the average spending per customer type?
* What is the average transaction per payment type?
* What is the hourly trend of sale recorded for each day?
* What are the top products by sales amount and quantity sold?
* What is the distribution of each product category sold per each day and hour?
</details>


<details>
<summary>Statistical Analysis</summary>
<br>
To ascertain that the  different in the average sale amount between customers who use credit cards and customers who use cash and the estimated_stock_pct of hour with sale activities greater than hour without sale activities for specific product do not occur by chance. To do this I performed hypothesis testing(Welch's t-Test) to draw conclusion on .
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
At the end of this project, we were able to draw the following unique insights:

* The distribution of `temperature` and `estimated_stock_pct` is normal distribution, this means the `mean` and the `median` are equal, and the data points are evenly distributed on both side of the `mean`
* The distribution of `tota` and `unit_price` are positively skewed. This means that there are relatively fewer data points with extremely high values compared to the majority of data points, which tend to cluster toward the lower end of the distribution and also the `median` is lower than the `mean`
* Fruit & vegetables are the 2 most frequently bought product categories 
* Non-members & standard are the most frequent buyers within the store
* Tuesday and Thursday are the two most frequent day for shopping 
* Cash is the most frequently used payment method
* The hour of 11 has the highest sale recorded and sale mostly drop from the hour of 11 to V-turn at hour of 15.
* `Premium` customers have highest average spending. There is no slight difference in the average  spending amount of customers. Though `non-member` customers buy frequently, however the `average` spending of `premium` customer are higher than the average spending of `non-member`. 
*  `Medicine` has the highest average total sales of `42.77`
* `Cash` has the highest average total sales of `20.37`
* `Kitchen`, `meat` and `seafood` are the top three product categories by total sales amount of `14,456.65`, `14,102.31` and `10754.81` respectively
* `Fruit` & `vegetables` are the top 2 bought product categories by quantity sold

Base on the hypothesis test
* You cannot conclude at the 5% significance level that There is a difference in the average sale amount between customers who use credit cards and customers who use cash.
* You can conclude at the 5% significance level that the `mean estimated_stock_pct` of products with sale activities is greater than  the mean `estimated_stock_pct` of products without sale activities at specific time of the day.

The final model gave `mean absolute error` (MAE) of 0.2195 which suggests that, on average, the model's predictions are off from the actual values by approximately 0.2195 units. We found out that `unit_price`, `temperature`, `total`, and `hour` of the day were more important in predicting stock level. We recommend that the the dataset needs to be further engineered, or more datasets need to be added.

In conclusion, we have been able to achieved our 2 main goals and have also tested our inital hypothesis.
<br>

## Certificate<a name="cf"></a> 
[Earned Certificate](https://insidesherpa.s3.amazonaws.com/completion-certificates/ANZ/ZLJCsrpkHo9pZBJNY_ANZ_tCfFoXSNJ4aLnBQye_completion_certificate.pdf)
