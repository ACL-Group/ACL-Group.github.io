reset
unset log
unset label
set xlabel 'Number of stock traders'
set xtics (3,6,9,12,15)
set key left top
#
set ylabel 'Memory cost (MB)'
set terminal postscript eps "Helvetica" 25
set out 'st-mem.eps'
plot 'st.dat' using 1:8 title 'Average' with linespoints lw 4 ps 3, 'st.dat' using 1:9 title 'Maximum' with linespoints lw 4 ps 3, 'st.dat' using 1:10 title 'Minimum' with linespoints lw 4 ps 3

reset
unset log
unset label
set xlabel 'Number of stock traders'
set xtics (3,6,9,12,15)
set key left top
#
set ylabel 'Maximum number of worlds'
set terminal postscript eps "Helvetica" 25
set out 'st-world.eps'
plot 'st.dat' using 1:5 title 'Average' with linespoints lw 4 ps 3, 'st.dat' using 1:6 title 'Maximum' with linespoints lw 4 ps 3, 'st.dat' using 1:7 title 'Minimum' with linespoints lw 4 ps 3

reset
unset log
unset label
set xlabel 'Number of stock traders'
set xtics (3,6,9,12,15)
set key left top
#
set ylabel 'CPU time (sec)'
set terminal postscript eps "Helvetica" 25
set out 'st-cpu.eps'
plot 'st.dat' using 1:2 title 'Average' with linespoints lw 4 ps 3, 'st.dat' using 1:3 title 'Maximum' with linespoints lw 4 ps 3, 'st.dat' using 1:4 title 'Minimum' with linespoints lw 4 ps 3

reset
unset log
unset label
set key left top
#
set xlabel '% time savings'
set ylabel 'Number of agents'
set xtics (0,10,20,30,40,50,60,70,80,90,100)
set terminal postscript eps "Helvetica" 25
set out 'st-exit.eps'
plot "st-exit.dat" u 1:2 with boxes title "" lw 4
