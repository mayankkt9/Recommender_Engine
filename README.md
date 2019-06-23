# Recommender_Engine


## Correlations Implementation -

In our model we’ll use the item based because we are considering that a user based system could be influenced by the change of film taste in the time by people and also because having less films than items, will fasten our calculations.
The correlation is a numerical values between -1 and 1 that indicates how much two variables are related to each other. Correlation = 0 means no correlation, while >0 is positive correlation and <0 is negative correlation

Pandas makes it very easy for us, (corrwith function) - We will get Item Item based table, with values represnting correlation i.e how similar movies are.
![alt text](https://github.com/mayankkt9/Recommender_Engine/blob/master/Correlation/Correlation_Matrix_demo.png?raw=true)

Now that we have the Correlation Matrix comes the fun part, where we have to suggest to the user which are the films (output of our system) that best match with his previous preferences (that will be the input of our system).

we’ll consider all the columns corresponding to the film the user already watched, for each column, we’ll drop the Nan Values. Once we have the values, we can consider to multiply each value for the rating considering it as weight (we’ll increase correlation, that will not be anymore between -1 and 1, for the film that user liked with higher rating) and after we’ll append all the values of all the columns considered in a Series “user_corr”.
Once we have the final Series, we can ordered the values in descending order (ascending=False) and suggest the first 5 films or how many films we want.

https://www.sciencedirect.com/science/article/pii/S0950705113003560
