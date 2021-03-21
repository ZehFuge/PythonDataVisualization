# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import pickle

#-Lesson---2-----------------------------------------------------------------------------------------------------------#
# # Lessongroup: 1 Bar Chart
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
# # plt.show()
#
#-Lesson---3-----------------------------------------------------------------------------------------------------------#
# # Lessongroup: 1 Bar Chart
# plt.title("Balance chart of 2017") # adds a title to the created plot
# plt.ylabel("Sold fruits (in 1k)") # adds a label for the y coordinate for better understanding of the output
#
# # replaces the x values (list) with other values (list of same length)
# # in this case, the numbers of the x axis are being replaced by the actual fruit names
# # plt.xticks(values_of_x_axis, new_values_for_x_axis
# plt.xticks(bar_coords, fruit)
#
# # plt.show()
#
#-Lesson-4-------------------------------------------------------------------------------------------------------------#
# # Lessongroup: 2 Horizontal Bar Chart
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
#-Lesson-5-------------------------------------------------------------------------------------------------------------#
# # Lessongroup: 3 Pie Chart
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
#-Lesson-6-------------------------------------------------------------------------------------------------------------#
# # Lessongroup: 4 Line Chart



plt.show()
