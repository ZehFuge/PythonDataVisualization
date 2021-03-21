# -*- coding: utf-8 -*-
from bokeh.io import show
from bokeh.plotting import figure
from bokeh.io import output_file

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

output_file("bar.html")

with open("coding-exp-by-dev-type.pickle", "rb") as f:
    data = pickle.load(f)

# split sublists
dev_types, years_exp = zip(*data)

plot = figure(y_range=dev_types, x_axis_label="Years", title="Coding Experience by Developer Type")
plot.hbar(y=dev_types, right=years_exp, height=0.75)

show(plot)
