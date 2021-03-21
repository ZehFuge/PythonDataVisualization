# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import pickle

#-Lesson---2-----------------------------------------------------------------------------------------------------------#
# # Topic: Bar Chart
# # load our data (rb means read binary data)
# with open("fruit-sales.pickle", "rb") as f:
#     # load sample list filled with tuples of fruits and their quantity
#     data = pickle.load(f)
# f.close()
#
# # split the list of tuples in two lists
# fruit, num_sold = zip(*data)
# bar_coords = range(len(fruit)) # save length of given data for graphical bar x orientations
#
# # save values to plot to be able to be shown, kind of plot valuebar (bar())
# # plt.bar(values_for_x_axis, values_for_y_axis)
# plt.bar(bar_coords, num_sold)
# # show the created bar plot object by calling plt
# plt.show()
#
# -Lesson---3-----------------------------------------------------------------------------------------------------------#
# # Topic: Labeling a Chart
# load our data (rb means read binary data)
# with open("fruit-sales.pickle", "rb") as f:
#     # load sample list filled with tuples of fruits and their quantity
#     data = pickle.load(f)
# f.close()
#
# # split the list of tuples in two lists
# fruit, num_sold = zip(*data)
# bar_coords = range(len(fruit)) # save length of given data for graphical bar x orientations
#
# # save values to plot to be able to be shown, kind of plot valuebar (bar())
# # plt.bar(values_for_x_axis, values_for_y_axis)
# plt.bar(bar_coords, num_sold)
# plt.title("Balance chart of 2017") # adds a title to the created plot
# plt.ylabel("Sold fruits (in 1k)") # adds a label for the y coordinate for better understanding of the output
#
# # replaces the x values (list) with other values (list of same length)
# # in this case, the numbers of the x axis are being replaced by the actual fruit names
# # plt.xticks(values_of_x_axis, new_values_for_x_axis)
# plt.xticks(bar_coords, fruit)
#
# plt.show()
#
# -Lesson-4-------------------------------------------------------------------------------------------------------------#
# # Topic: Horizontal Bar Chart
#
# # load data like in lesson 2
# with open("coding-exp-by-dev-type.pickle", "rb") as f:
#     data = pickle.load(f)
# f.close()
#
# # split data again
# dev_types, years_exp = zip(*data)
# bar_coords = range(len(dev_types)) # safe amount of dev_types as a list
#
# # bar = bar chart, barh = horizontal bar chart
# plt.barh(bar_coords, years_exp)
# plt.title("Years of Coding Experience by Developer Type")
# plt.xlabel("Years")
# plt.yticks(bar_coords, dev_types, fontsize=8) # see lesson 3
#
# plt.tight_layout() # if there are long texts, it makes them displayed completly on the created graph
# plt.show()
#
# -Lesson-5-------------------------------------------------------------------------------------------------------------#
# # Topic: Pie Chart
#
# # load data
# with open("devs-outside-time.pickle", "rb") as f:
#     data = pickle.load(f)
# f.close()
# print(data)
#
# # split into two lists
# time, responses = zip(*data)
#
# # create pie chart
# # plt.pie(values_for_pies, labels=pie_names, autopct=fill_pies_with_data)
# # autopct="%f%%" - fills the pies with their percentage value as float number
# # autopct="%.2f%%" - like the above, but round to two decimal points for better readability
# plt.pie(responses, labels=time, autopct="%.2f%%")
# plt.axis("equal") # sets proportions equally if pie chart looks like an eclipse
# plt.title("Daily Time Developers Spend Outside")
#
# plt.show()
#
# -Lesson-6-------------------------------------------------------------------------------------------------------------#
# # Topic: Line Chart
#
# # load data
# with open("prog-langs-popularity.pickle", "rb") as f:
#     data = pickle.load(f)
#
# # split into two lists
# languages, rankings = zip(*data)
#
# # get the Java years and ranks
# java_years, java_ranks = zip(*rankings[0])
#
# plt.plot(java_years, java_ranks)
# plt.xticks(java_years) # set x-axis values to java_years list
# # x-axis: year, y-axis: ranking, title: Java Ranking
# plt.xlabel("Year")
# plt.ylabel("Ranking")
# plt.title("Java Ranking")
# plt.show()
#
# -Lesson-7-------------------------------------------------------------------------------------------------------------#
# # Topic: Multiline Charts
#
# with open("prog-langs-popularity.pickle", "rb") as f:
#     data = pickle.load(f)
#
# # split int two lists
# languages, rankings = zip(*data)
#
# # iterate over all of the language and call "plot" on their data
# for i in range(len(languages)):
#     # for each language, split their data into years and rankings lists
#     years, ranks = zip(*rankings[i])
#     plt.plot(years, ranks) # set plots for each language
#
# # x-axis: year, y-axis: ranking, title: Rankings of Programming Languages
# plt.xlabel("Year")
# plt.ylabel("Ranking")
# plt.title("Rankings of Programming Languages")
# plt.legend(languages) # set a legend for better understanding of the graph
# plt.show()
#
# -Lesson-8-------------------------------------------------------------------------------------------------------------#
# # Topic: Scatter Plots Charts
#
# with open("iris.pickle", "rb") as f:
#     iris = pickle.load(f)
#
# # a set of iris["data"] = [[4.7, 3.0, 1.7, 0.3]]
# # [:] - take everthing from the list
# # [:, 0] - Read the whole list and get value from the first column (in example case: 4.7)
# sepal_length = iris["data"][:, 0] # sepal = Kelchblatt
# sepal_width = iris["data"][:, 1]
# classes = iris["target"] # get plant names
#
# """
# c - seperates values with different colors
#
# In this case, the list "classes" contains 150 values between 0 to 2. For every information, sepal_length,
# sepal_width, classes get iterated like in a for loop. E.x. If classes is 0, the dot is black, 1 means blue, 2 means
# yellow. So the output can be seperated by colors and being understanded. This means, every item in a data base needs
# an group indicator like numbers or strings (e.x. the animals list groups could be "dog", "cat", "mouse", "bird" etc.
# For examples, a list of regular lifespans can be seperated by the animal type.
# """
# plt.scatter(sepal_length, sepal_width, c=classes)
# plt.xlabel("Sepal length (cm)")
# plt.ylabel("Sepal width (cm)")
# plt.show()
#
# -Lesson-9-------------------------------------------------------------------------------------------------------------#
# Topic: Multiline Plots in One Figure

with open("iris.pickle", "rb") as f:
    iris = pickle.load(f)

# a set of iris["data"] = [[4.7, 3.0, 1.7, 0.3]]
# [:] - take everthing from the list
# [:, 0] - Read the whole list and get value from the first column (in example case: 4.7)
sepal_length = iris["data"][:, 0] # sepal = Kelchblatt
sepal_width = iris["data"][:, 1]
petal_length = iris["data"][:, 2] # petal = Blütenblatt
petal_width = iris["data"][:, 3]
classes = iris["target"] # get plant names

"""
A figure object with an array of graphs is being created here. There will be two rows with two columns filled with
different graphs. This can be usefull if need the same kind of data for different situation for example. If you test
a new car, you will always get the same data: needed fuel, max kmh, min kmh. But you want this data in four different
conditions. Like driving on the street, sand, dirt and ice. So you dont get four different graph windows, but one
with every information and situation needed.

Accessing the graphs (2, 2) with:
upperleft: axes[0,0]           upperright: axes[0,1]
lowerleft: axes[1,0]           lowerright: axes[1,1]
"""
fig, axes = plt.subplots(2, 2)
# first graph
# sepal length vs sepal width
axes[0,0].scatter(sepal_length, sepal_width, c=classes)
axes[0,0].set_xlabel("Sepal lenght (cm)")
axes[0,0].set_ylabel("Sepal width (cm)")

# second graph
# petal length vs petal width
axes[0,1].scatter(petal_length, petal_width, c=classes)
axes[0,1].set_xlabel("petal lenght (cm)")
axes[0,1].set_ylabel("petal width (cm)")

# third graph
# sepal length vs petal length
axes[1,0].scatter(sepal_length, petal_length, c=classes)
axes[1,0].set_xlabel("sepal lenght (cm)")
axes[1,0].set_ylabel("petal lenght (cm)")

# fourth graph
# sepal width vs petal width
axes[1,1].scatter(sepal_width, petal_width, c=classes)
axes[1,1].set_xlabel("sepal width (cm)")
axes[1,1].set_ylabel("petal width (cm)")

fig.suptitle("Iris dataset") # set title for the while figure containing the four graphs
plt.show()
