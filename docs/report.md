Link to the powerpoint: https://1drv.ms/p/s!AlANcVqkc7WmgYE0L-shgIKxQNwTPA

## Abstract
•	The real estate industry is one of the most competitive in terms of pricing and is always changing. 
•	It is one of the key areas where machine learning concepts are applied to improve and accurately predict expenses. 
•	Predicting a real estate property's market worth is the paper's main goal. This approach aids in determining a property's beginning price depending on geographic factors. 
•	There is even a possibility to predict future cost. 
•	by dissecting past market trends, price ranges, and upcoming technological improvements. 

## About the Data
So I picked the dataset from Kaggle. This dataset is about organizing a sizable collection of real estate sales records that are kept in unknown format and have unknown data quality issues based on the info supplied.
Data Overview This dataset
is made up of 18 columns, with dtypes: float64(4), int64(9), object(5) memory usage:
647.0+ KB.
The columns are price, bedrooms, bathrooms, sqft_living, sqft_lot, floors, waterfront, view, condition, sqft_above, sqft_basement, yr_built, yr_renovated, street, city, statezip, and country. This Data is for America as a whole, from 2005 to 2022

## Preprocessing
•	Got rid of nulls
•	Got rid of duplicates 
•	Got rid of columns I did not want to use
•	Just because I wanted to use a few features only for my project. So I got rid of waterfront, country, street, state zip, and city 
•	Then executed the describe function and as you can see, I could infer a few things. 
•	Looking at the bedroom columns , the dataset has a house where the house has 33 bedrooms , seems to be a massive house and would be interesting to know more about it as I progress.
•	I also noticed Maximum square feet is 13,450 where as the minimum is 290. This tells me that the data is distributed

## How common factors are affecting the price of the houses ?
•	for the condition feature for example, From the plot we notice that the higher the price the better the condition of the house.,I mean who will wanna buy a house at the high price if it is not in a good condition
•	the more the basement squarefeet , more the price though data is concentrated towards a particular price zone , but from the figure we can see that the data points seem to be in linear direction. Thanks to scatter plot we can also see some irregularities that the house with the highest square feet was sold for very less , maybe there is another factor or probably the data must be wrong. 

## Model
•	Now that I got familiar with all these representation and can kinda tell my own story i moved and created a model that would predict the price of the house based upon the those factors.

•	For me, I decided with bedrooms, bathrooms condition and the zipcode.  And I decided to use linear regression 

•	Here are my dependent and independent variables.
 Dependent variable: “Price”
      Independent variables: Bedrooms, bathrooms, condition, and Zipcode
•	Then fitted and saved the model. I want to precise that Usually, I’d need to wrangle the data, train, and validate the results, but to make things simple, for the project I only wanted to focus on fitting and deploying the model only.

## Deployment
•	Now that all of that was looking good
•	now I wanted to deploy all of this on a website, so anyone can play with our model right. 
•	So I decided I’ll send everything from the backend to the frontend with Flask in the next section, 
•	but before we do that let’s save my lm model with pickle.
•	So remember, as shown above, in the previous slide, lm.predict() accepts inputs in dataframe format [[]].
•	In order to accomplish this is used another environment called pycharm 
•	Working with different environments will helped me better manage the different resources required for building the model and deploying the web app.
•	I set up a virtual environment called “deploy-mlmodel-env., ran a command on my terminal 

## web app
•	Created a file called app.py
•	Imported Flask, and other libraries
•	Then loaded my linear regression model that I saved with pickle
•	Then I had an html file named index.html
•	The index.html file will contain the front end of the website (navigation bar, buttons, images, etc.).
•	Did not think to really go into the details of my html file in the presentation,so you can check out my github for more details

The app is not 100% accurate as there were some issues I have not been able to fix yet 

