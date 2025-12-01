
import matplotlib.pyplot as plt

import psycochart as psycochart

#code to generate graph 

#x-limits unit - temperature

#y-limits unit - [kg of water vapor /kg of dry air]

#'y' stands for yes 

#'p' = pressure [N/m^2] 

figure,axes = psycochart.plot_psy_chart(x_low_limit = -10,x_upp_limit = 60,y_low_limit = 0,y_upp_limit = 0.03, p = 101325, RH_lines = 'y',H_lines = 'y',WB_lines = 'y')

a = [[50,0.007],[40, 0.006],[30,0.003]] # list 'a'

figure,axes = psycochart.plot_points(a,figure,axes, col = 'r', typ = '-', grid = 'on') #code to plot points in list 'a'

axes.plot()