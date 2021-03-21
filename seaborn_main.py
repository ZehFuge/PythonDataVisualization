# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import pickle
import seaborn as sns

#-Lesson-10------------------------------------------------------------------------------------------------------------#
# # Topic: Coulmn and Bar Chart
# with open("fruit-sales.pickle", "rb") as f:
#     data = pickle.load(f)
# f.close()
#
# # splitting list of tuples into two lists
# fruit, num_sold = zip(*data)
# fruit = list(fruit)
# num_sold = list(num_sold)
#
# axes = sns.barplot(x=fruit, y=num_sold)
# axes.set_title("Number of fruits sold in 2017")
# axes.set_ylabel("Number of sold fruits (millions)")
#
# # sample code of lesson 4 converted to seaborn way
# with open("coding-exp-by-dev-type.pickle", "rb") as f:
#     data = pickle.load(f)
# f.close()
#
# plt.show()
#
# #
# # split data again
# dev_types, years_exp = zip(*data)
# dev_types = list(dev_types)
# years_exp = list(years_exp)
#
# # by adding the y-axis first, the bar chart became a horizontal bar chart
# axes2 = sns.barplot(y=dev_types, x=years_exp)
# axes2.set_title("Years of Coding Experience by Developer Type")
# axes2.set_xlabel("Years")
#
# plt.tight_layout() # if there are long texts, it makes them displayed completly on the created graph
#
# plt.show()

#-Lesson-11------------------------------------------------------------------------------------------------------------#
# # Topic: Line Plot Chart
#
# # load data
# with open("prog-langs-popularity.pickle", "rb") as f:
#     data = pickle.load(f)
# f.close()
#
# # split into two lists
# languages, rankings = zip(*data)
#
# # get the Java years and ranks
# java_years, java_ranks = zip(*rankings[0])
#
# # convert to list
# java_ranks = list(java_ranks)
# java_years = list(java_years)
#
# axes = sns.lineplot(x=java_years, y=java_ranks)
# plt.xticks((java_years))
# axes.set_title("Java Ranking")
# axes.set_xlabel("Year")
# axes.set_ylabel("Ranking")
#
# plt.show()

#-Lesson-12------------------------------------------------------------------------------------------------------------#
# # Topic: Scatter Plot Chart & Multiple Plots Figure
#
# with open("iris.pickle", "rb") as f:
#     iris = pickle.load(f)
# f.close()
#
# sepal_length = iris["data"][:, 0] # sepal = Kelchblatt
# sepal_width = iris["data"][:, 1]
# classes = iris["target"] # get plant names
#
# axes = sns.scatterplot(x=sepal_length, y=sepal_width, hue=classes, legend=False)
# axes.set_ylabel("Sepal width (cm)")
# axes.set_xlabel("Sepal length (cm)")
#
# plt.show()
#
# # convert lesson 9 to seaborn way
# with open("iris.pickle", "rb") as f:
#     iris = pickle.load(f)
# f.close()
#
# sepal_length = iris["data"][:, 0] # sepal = Kelchblatt
# sepal_width = iris["data"][:, 1]
# petal_length = iris["data"][:, 2] # petal = Blütenblatt
# petal_width = iris["data"][:, 3]
# classes = iris["target"] # get plant names
#
# fig, axes = plt.subplots(2, 2)
# sns.scatterplot(x=sepal_length, y=sepal_width, hue=classes, legend=False, ax=axes[0,0])
# axes[0,0].set_xlabel("Sepal lenght (cm)")
# axes[0,0].set_ylabel("Sepal width (cm)")
#
# # second graph
# # petal length vs petal width
# sns.scatterplot(x=petal_length, y=petal_width, hue=classes, legend=False, ax=axes[0,1])
# axes[0,1].set_xlabel("petal lenght (cm)")
# axes[0,1].set_ylabel("petal width (cm)")
#
# # third graph
# # sepal length vs petal length
# sns.scatterplot(x=sepal_length, y=petal_length, hue=classes, legend=False, ax=axes[1,0])
# axes[1,0].set_xlabel("sepal lenght (cm)")
# axes[1,0].set_ylabel("petal lenght (cm)")
#
# # fourth graph
# # sepal width vs petal width
# sns.scatterplot(x=sepal_width, y=petal_width, hue=classes, legend=False, ax=axes[1,1])
# axes[1,1].set_xlabel("sepal width (cm)")
# axes[1,1].set_ylabel("petal width (cm)")
#
# fig.suptitle("Iris dataset") # set title for the while figure containing the four graphs
# plt.show()

#-Lesson-13------------------------------------------------------------------------------------------------------------#
# Topic: Join Plot Charts

with open("iris.pickle", "rb") as f:
    iris = pickle.load(f)
f.close()

sepal_length = iris["data"][:, 0]
sepal_width = iris["data"][:, 1]
classes = iris["target"]

# kind=["scatter", "reg", "resid", "kde", "hex]
axes = sns.jointplot(x=sepal_length, y=sepal_width, kind="hex")
axes.set_axis_labels("Sepal length (cm)", "Sepal width (cm)")

plt.tight_layout()
plt.show()
