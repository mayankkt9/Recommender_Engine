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


## Cosine Similarity


Cosine similarity measures the similarity between two vectors by taking the cosine of the angle the two vectors make in their dot product space. If the angle is zero, their similarity is one, the larger the angle is, the smaller their similarity. The
measure is independent of vector length (the two vectors can even be of different length), which makes it a commonly used measure for high-dimensional spaces. For example, in case of movie recoomendation, we would compare the rating of two users for a particular movie and observe how similar they are.

For example : user A gave 4/5 for HarryPotter 1
			  user B gave 1/5 for HarryPotter 1
			  user C gave 5/5 for HarryPotter 1

Hence, user A and user C are more similar than user A and user B based on cosine similarity

Cosine similarity is computed using the following formula:
![alt text](https://wikimedia.org/api/rest_v1/media/math/render/svg/1d94e5903f7936d3c131e040ef2c51b473dd071d)


cosine similarity values range between -1 and 1, where -1 is perfectly dissimilar and 1 is perfectly similar.


