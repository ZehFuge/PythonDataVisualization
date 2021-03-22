# -*- coding: utf-8 -*-
from bokeh.io import show # used to show the created graphs
from bokeh.plotting import figure # to create figure e.x. for multi plot charts
from bokeh.io import output_file # safes the output to an file, in this case .html
from bokeh.palettes import Dark2_5 as palette # imports the Dark2 palette with 5 colors
from bokeh.layouts import row, column, gridplot # used for multiline plots
import pickle

#-Lesson-14------------------------------------------------------------------------------------------------------------#
# # Topic: Column Chart
#
# with open("fruit-sales.pickle", "rb") as f:
#     data = pickle.load(f)
#
# # split into two lists
# fruit, num_sold = zip(*data)
#
# plot = figure(x_range=fruit, y_axis_label="Fruit sold (millions)", title="Fruit sold (2017)")
# plot.vbar(x=fruit, top=num_sold, width=0.9)
#
# show(plot)

#-Lesson-15------------------------------------------------------------------------------------------------------------#
# # Topic: Bar Chart
#
# output_file("bar.html")
#
# with open("coding-exp-by-dev-type.pickle", "rb") as f:
#     data = pickle.load(f)
#
# # split sublists
# dev_types, years_exp = zip(*data)
#
# plot = figure(y_range=dev_types, x_axis_label="Years", title="Coding Experience by Developer Type")
# plot.hbar(y=dev_types, right=years_exp, height=0.75)
#
# show(plot)

#-Lesson-16------------------------------------------------------------------------------------------------------------#
# # Topic: Adding Tooltips to Chart
#
# output_file("Lesson_16_Tooltips.html")
#
# with open("coding-exp-by-dev-type.pickle", "rb") as f:
#     data = pickle.load(f)
# f.close()
#
# # split data again
# dev_types, years_exp = zip(*data)
#
# # sets links to vars
# data_source = {"dev_types": dev_types, "years_exp": years_exp}
#
# # tool tips: "years of experience: actual val"
# # TOOLTIPS = [("Displayed Text", "@var_from_data_source")]
# TOOLTIPS = [("Years of experience", "@years_exp")]
#
# # adding the created TOOLTIPS with the "tooltips" keyword
# plot = figure(y_range=dev_types,
#               x_axis_label="Years",
#               title="Coding Experience by Developer Types",
#               tools="hover",
#               tooltips=TOOLTIPS)
#
# # adding the source for the linked data
# plot.hbar(y="dev_types",
#           right="years_exp",
#           height=0.9,
#           source=data_source)
#
# show(plot)

#-Lesson-17------------------------------------------------------------------------------------------------------------#
# # Topic: Multiline Plots
#
# output_file("Lesson_17_Multiline_Plot_Chart.html")
#
# with open("prog-langs-popularity.pickle", "rb") as f:
#     data = pickle.load(f)
#
# # splitting
# languages, rankings = zip(*data)
#
# fig = figure(x_axis_label="Year",
#              y_axis_label="Rank",
#              title="Ranking of popular languages")
#
# for i in range(len(languages)):
#     years, ranks = zip(*rankings[i])
#     fig.line(x=years, y=ranks,
#              line_width=2,
#              legend_label=languages[i],
#              color=palette[i])
#
# show(fig)

#-Lesson-18------------------------------------------------------------------------------------------------------------#
# # Topic: Interactive Legends
#
# output_file("Lesson_18_Interactive_Legends.html")
#
# with open("prog-langs-popularity.pickle", "rb") as f:
#     data = pickle.load(f)
#
# # splitting
# languages, rankings = zip(*data)
#
# fig = figure(x_axis_label="Year",
#              y_axis_label="Rank",
#              title="Ranking of popular languages")
#
# for i in range(len(languages)):
#     years, ranks = zip(*rankings[i])
#     fig.line(x=years, y=ranks,
#              line_width=2,
#              legend_label=languages[i],
#              color=palette[i])
#
# # interactive legend:
# fig.legend.click_policy = "hide"
#
# show(fig)

#-Lesson-19------------------------------------------------------------------------------------------------------------#
# # Topic: Scatter Plot Chart
#
# output_file("Lesson_19_Scatter_Plot_Chart.html")
#
# with open("iris.pickle", "rb") as f:
#     iris = pickle.load(f)
#
# sepal_length = iris["data"][:, 0] # sepal = Kelchblatt
# sepal_width = iris["data"][:, 1]
# classes = iris["target"] # get plant names
#
# # seperate data via classes
# setosa_sepal_length = sepal_length[classes == 0]
# setosa_sepal_width = sepal_width[classes == 0]
# versicolor_sepal_length = sepal_length[classes == 1]
# versicolor_sepal_width = sepal_width[classes == 1]
# virginca_sepal_length = sepal_length[classes == 2]
# virginca_sepal_width = sepal_width[classes == 2]
#
# fig = figure(x_axis_label="Sepal length (cm)",
#              y_axis_label="Sepal width (cm)")
#
# # plot the setosa sepal length vs width
# fig.circle(x=setosa_sepal_length, y=setosa_sepal_width,
#            color=palette[0],
#            legend_label="Setosa")
#
# # plot the versicolor sepal length vs width
# fig.circle(x=versicolor_sepal_length, y=versicolor_sepal_width,
#            color=palette[1],
#            legend_label="Versicolor")
#
# # plot the virginica sepal length vs width
# fig.circle(x=virginca_sepal_length, y=virginca_sepal_width,
#            color=palette[2],
#            legend_label="Virginica")
#
# show(fig)

#-Lesson-20------------------------------------------------------------------------------------------------------------#
# # Topic: Multiline Plot Charts
#
# output_file("Lesson_20_Multiline_Plot_Chart_With_Blank.html")
#
# with open("iris.pickle", "rb") as f:
#     iris = pickle.load(f)
#
# sepal_length = iris["data"][:, 0]
# sepal_width = iris["data"][:, 1]
# petal_length = iris["data"][:, 2]
# petal_width = iris["data"][:, 3]
# classes = iris["target"]
#
# # seperate data via classes
# setosa_sepal_length = sepal_length[classes == 0]
# setosa_sepal_width = sepal_width[classes == 0]
# setosa_petal_length = petal_length[classes == 0]
# setosa_petal_width = petal_width[classes == 0]
#
# versicolor_sepal_length = sepal_length[classes == 1]
# versicolor_sepal_width = sepal_width[classes == 1]
# versicolor_petal_length = petal_length[classes == 1]
# versicolor_petal_width = petal_width[classes == 1]
#
# virginca_sepal_length = sepal_length[classes == 2]
# virginca_sepal_width = sepal_width[classes == 2]
# virginca_petal_length = petal_length[classes == 2]
# virginca_petal_width = petal_width[classes == 2]
#
#
#
# # plot the sepal lengths vs widths
# fig1 = figure(x_axis_label="Sepal length (cm)",
#              y_axis_label="Sepal width (cm)")
# fig1.circle(x=setosa_sepal_length, y=setosa_sepal_width,
#            color=palette[0],
#            legend_label="Setosa")
# fig1.circle(x=versicolor_sepal_length, y=versicolor_sepal_width,
#            color=palette[1],
#            legend_label="Versicolor")
# fig1.circle(x=virginca_sepal_length, y=virginca_sepal_width,
#            color=palette[2],
#            legend_label="Virginca")
#
# # plot the petal lengths vs widths
# fig2 = figure(x_axis_label="Petal length (cm)",
#              y_axis_label="Petal width (cm)")
# fig2.circle(x=setosa_petal_length, y=setosa_petal_width,
#            color=palette[0],
#            legend_label="Setosa")
# fig2.circle(x=versicolor_petal_length, y=versicolor_petal_width,
#            color=palette[1],
#            legend_label="Versicolor")
# fig2.circle(x=virginca_petal_length, y=virginca_petal_width,
#            color=palette[2],
#            legend_label="Virginca")
#
# # plot the sepal lengths vs petal lengths
# fig3 = figure(x_axis_label="Sepal length (cm)",
#              y_axis_label="Petal length (cm)")
# fig3.circle(x=setosa_sepal_length, y=setosa_petal_length,
#            color=palette[0],
#            legend_label="Setosa")
# fig3.circle(x=versicolor_sepal_length, y=versicolor_petal_length,
#            color=palette[1],
#            legend_label="Versicolor")
# fig3.circle(x=virginca_sepal_length, y=virginca_petal_length,
#            color=palette[2],
#            legend_label="Virginca")
#
# # plot the sepal widths vs petal widths
# fig4 = figure(x_axis_label="Sepal width (cm)",
#              y_axis_label="Petal width (cm)")
# fig4.circle(x=setosa_sepal_width, y=setosa_petal_width,
#            color=palette[0],
#            legend_label="Setosa")
# fig4.circle(x=versicolor_sepal_width, y=versicolor_petal_width,
#            color=palette[1],
#            legend_label="Versicolor")
# fig4.circle(x=virginca_sepal_width, y=virginca_petal_width,
#            color=palette[2],
#            legend_label="Virginca")
#
#
# # !!! ONLY DISPLAY ONE OF THE TWO SHOW() COMMANDS !!!
#
# # shows all four created graphs
# show(gridplot([[fig1, fig2],
#                [fig3, fig4]]))
#
# # # shows three created graphs and leaves one blank place
# # show(gridplot([[fig1, fig2],
# #                [None, fig4]]))

#-Lesson-21------------------------------------------------------------------------------------------------------------#
# # Topic: Linked Panning

output_file("Lesson_21_Linked_Panning.html")

with open("iris.pickle", "rb") as f:
    iris = pickle.load(f)

sepal_length = iris["data"][:, 0]
sepal_width = iris["data"][:, 1]
petal_length = iris["data"][:, 2]
petal_width = iris["data"][:, 3]
classes = iris["target"]

# seperate data via classes
setosa_sepal_length = sepal_length[classes == 0]
setosa_sepal_width = sepal_width[classes == 0]
setosa_petal_length = petal_length[classes == 0]
setosa_petal_width = petal_width[classes == 0]

versicolor_sepal_length = sepal_length[classes == 1]
versicolor_sepal_width = sepal_width[classes == 1]
versicolor_petal_length = petal_length[classes == 1]
versicolor_petal_width = petal_width[classes == 1]

virginca_sepal_length = sepal_length[classes == 2]
virginca_sepal_width = sepal_width[classes == 2]
virginca_petal_length = petal_length[classes == 2]
virginca_petal_width = petal_width[classes == 2]



# plot the sepal lengths vs widths
fig1 = figure(x_axis_label="Sepal length (cm)",
             y_axis_label="Sepal width (cm)")
fig1.circle(x=setosa_sepal_length, y=setosa_sepal_width,
           color=palette[0],
           legend_label="Setosa")
fig1.circle(x=versicolor_sepal_length, y=versicolor_sepal_width,
           color=palette[1],
           legend_label="Versicolor")
fig1.circle(x=virginca_sepal_length, y=virginca_sepal_width,
           color=palette[2],
           legend_label="Virginca")

# plot the petal lengths vs widths
# x/y_range sets the current x and y position of the other graph
# this is usefull, if two graphs information are liked to each other / are related to each other
# and set them linked, increases the readablity of the user of the data
fig2 = figure(x_axis_label="Petal length (cm)",
             y_axis_label="Petal width (cm)",
              x_range=fig1.x_range,
              y_range=fig1.y_range)
fig2.circle(x=setosa_petal_length, y=setosa_petal_width,
           color=palette[0],
           legend_label="Setosa")
fig2.circle(x=versicolor_petal_length, y=versicolor_petal_width,
           color=palette[1],
           legend_label="Versicolor")
fig2.circle(x=virginca_petal_length, y=virginca_petal_width,
           color=palette[2],
           legend_label="Virginca")

# shows all four created graphs
show(row([fig1, fig2]))
