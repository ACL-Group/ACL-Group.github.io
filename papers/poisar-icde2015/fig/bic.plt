set terminal postscript eps linewidth 2 "Helvetica" 24
set xlabel "A"
set xrange [10:50] reverse
set xtics 0,10,50
set ylabel "R"
set ytics 0,20,100
#set zlabel "BIC"
set ztics 1e+006
set xyplane 0.2
set hidden3d
#set view 45,60
unset key
set output "bic_p.eps"
splot "bic_ph.dat" with lines
unset output
set term wxt