#!/usr/bin/python 

""" 
    Skeleton code for k-means clustering mini-project.
"""




import pickle
import numpy
import matplotlib.pyplot as plt
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
from sklearn.cluster import KMeans
from datetime import datetime
import re



def Draw(pred, features, poi, mark_poi=False, name="image.png", f1_name="feature 1", f2_name="feature 2"):
    """ some plotting code designed to help you visualize your clusters """

    ### plot each cluster with a different color--add more colors for
    ### drawing more than five clusters
    colors = ["b", "r", "c", "k", "m", "g"]
    for ii, pp in enumerate(pred):
        plt.scatter(features[ii][0], features[ii][1], color = colors[pred[ii]])

    ### if you like, place red stars over points that are POIs (just for funsies)
    if mark_poi:
        for ii, pp in enumerate(pred):
            if poi[ii]:
                plt.scatter(features[ii][0], features[ii][1], color="r", marker="*")
    plt.xlabel(f1_name)
    plt.ylabel(f2_name)
    plt.savefig(name)
    plt.show()



### load in the dict of dicts containing all the data on each person in the dataset
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
### there's an outlier--remove it! 
data_dict.pop("TOTAL", 0)


### the input features we want to use 
### can be any key in the person-level dictionary (salary, director_fees, etc.) 
feature_1 = "salary"
feature_2 = "exercised_stock_options"
feature_3 = "total_payments"
poi  = "poi"
features_list = [poi, feature_1, feature_2]
#features_list = [poi, feature_1, feature_2, feature_3]
data = featureFormat(data_dict, features_list )
poi, finance_features = targetFeatureSplit( data )


### in the "clustering with 3 features" part of the mini-project,
### you'll want to change this line to 
### for f1, f2, _ in finance_features:
### (as it's currently written, the line below assumes 2 features)
#for f1, f2, _ in finance_features:
for f1, f2 in finance_features:
    plt.scatter( f1, f2 )
plt.show()

values_1 = []
values_2 = []
values_3 = []

for k in data_dict.keys():
    person = data_dict[k]
    values_1.append(float(person[feature_1]))
    values_2.append(float(person[feature_2]))
    values_3.append(float(person[feature_3]))

min_max_1 = (numpy.nanmin(values_1), numpy.nanmax(values_1))
min_max_2 = (numpy.nanmin(values_2), numpy.nanmax(values_2))
min_max_3 = (numpy.nanmin(values_3), numpy.nanmax(values_3))

print(feature_1 + ": " + str(min_max_1))
print(feature_2 + ": " + str(min_max_2))
print(feature_3 + ": " + str(min_max_3))

### cluster here; create predictions of the cluster labels
### for the data and store them to a list called pred

#k_means_object = KMeans(n_clusters=2)
#pred = k_means_object.fit_predict(finance_features)


### rename the "name" parameter when you change the number of features
### so that the figure gets saved to a different file
file_name = str(len(features_list) - 1) + "_features-" + re.sub('[-:. ]','',str(datetime.now())) 

try:
    Draw(pred, finance_features, poi, mark_poi=False, name=file_name, f1_name=feature_1, f2_name=feature_2)
except NameError:
    print "no predictions object named pred found, no clusters to plot"