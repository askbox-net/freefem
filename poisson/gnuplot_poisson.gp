set hidden3d
#set pm3d depthorder
#set dgrid3d
set term postscript eps enhanced color 20
set output "./outputs/gnuplot.eps"
set palette rgbformulae 33,13,10
splot "./outputs/gnuplot.gp" with lines palette

