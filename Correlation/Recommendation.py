import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('white')

rating_table=pd.read_csv("dataset_small/ratings.csv")
print(rating_table.head())


movie_table=pd.read_csv("dataset_small/movies.csv")
print(movie_table.head())

movie_rate_merge=pd.merge(rating_table,movie_table,on='movieId')
print(movie_rate_merge.head())

rating_mean=pd.DataFrame(movie_rate_merge.groupby('title')['rating'].mean())
print(rating_mean)

rating_mean['num of ratings'] = pd.DataFrame(movie_rate_merge.groupby('title')['rating'].count())
print(rating_mean)

plt.figure(figsize=(10,4))
rating_mean['num of ratings'].hist(bins=80)
#plt.show()

plt.figure(figsize=(10,4))
rating_mean['rating'].hist(bins=80)
#plt.show()

sns.jointplot(x='rating',y='num of ratings',data=rating_mean,alpha=0.5)
plt.show(sns)


moviemat = movie_rate_merge.pivot_table(index='userId',columns='title',values='rating')
print(moviemat.head())
moviemat.to_csv('output.csv')

print(rating_mean.sort_values('num of ratings',ascending=False).head(10))


fg_user_ratings = moviemat['Forrest Gump (1994)']
print(fg_user_ratings.head(30))

similar_to_fg = moviemat.corrwith(fg_user_ratings)
corr_fg = pd.DataFrame(similar_to_fg,columns=['Correlation'])
corr_fg.dropna(inplace=True)
print(corr_fg.head(20))

print(corr_fg.sort_values('Correlation',ascending=False).head(10))
corr_fg = corr_fg.join(rating_mean['num of ratings'])
print(corr_fg.head(10))

print(corr_fg[corr_fg['num of ratings']>100].sort_values('Correlation',ascending=False).head())


matrix_corr=moviemat.corr(method='pearson',min_periods=100)
print(matrix_corr.head(10))

print(moviemat.iloc[0].dropna())

user_corr=pd.Series()
user_id=0

for film in moviemat.iloc[user_id].dropna().index:
	corr_list=matrix_corr[film].dropna()*moviemat.iloc[user_id][film]
	user_corr=user_corr.append(corr_list)
	
user_corr=user_corr.groupby(user_corr.index).sum()

title_list=[]
for i in range(len(moviemat.iloc[user_id].dropna().index)):
	if moviemat.iloc[user_id].dropna().index[i] in user_corr:
		title_list.append(moviemat.iloc[user_id].dropna().index[i])
	
		
user_corr=user_corr.drop(title_list)

print('Hi, based on the film that you have seen: \n')
for i in moviemat.iloc[user_id].dropna().index:
	print(i)
	
print('\n I would suggest you to watch these films \n')
for i in user_corr.sort_values(ascending=False).index[:5]:
	print(i)




