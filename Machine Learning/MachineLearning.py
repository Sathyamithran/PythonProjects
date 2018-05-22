##importing the k-means clustering mmodel
from sklearn.cluster import KMeans

##importing of the pandas library.
import pandas

##importing matplotlib
import matplotlib.pyplot as plt

#read the data in the name of 'games' and store the values of 'added games.csv' in it
games = pandas.read_csv('added_games.csv')

##printing the names of the columns in games.
#print(games.columns)<---------remove #

#print(games.shape)<----------remove #

##this will extract the single column of the dataframe
#print(games['average_rating'])<------------remove #


## make a histogram of all the ratings in the 'average_rating' column
plt.hist(games['average_rating'])

##show the plot graph
#plt.show()<------------remove #

##print the first row of all the games with the zero scores
#print(games[games['average_rating'] == 0])<----------remove #

## the '.iloc' method on the dataframse allows us to index by position
#print(games[games['average_rating'] == 0].iloc[0])<---------remove #

## showing the games with score greater than 0
#print(games[games['average_rating'] > 0].iloc[0])<----------remove #

##removing the games without user reviews
#games = games[games["users_rated"] > 0]<------------remove #

##remove any rows with missing values.
#games = games.dropna(axis=0)<--------remove #

"""
#initialize the model with 2 parameters (no. of clusters and random state)
kmeans_model = KMeans(n_clusters = 5,random_state = 1)

#get only the numeric columns from the games.
good_columns = games._get_numeric_data()

#fit the model using the good columns.
kmeans_model.fit(good_columns)

#get the cluster assignments
labels = kmeans_model.labels_

print(labels)
"""
