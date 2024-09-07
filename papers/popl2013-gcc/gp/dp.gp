reset
unset log
unset label
set xlabel 'Number of dining philosophers'
set xtics (10,20,30,40)
set key left top
#
set ylabel 'Memory cost (MB)'
set terminal post eps enhanced "Helvetica" 25
set out 'dp-mem.eps'
plot 'dp.dat' using 1:2 title 'Average' with linespoints lw 8 ps 4, 'dp.dat' using 1:7 title 'Maximum' with linespoints lw 8 ps 4

reset
unset log
unset label
set xlabel 'Number of dining philosophers'
set xtics (10,20,30,40)
set key left top
#
set ylabel 'Maximum number of worlds'
set yrange [2:5]
set terminal post eps enhanced "Helvetica" 25
set out 'dp-world.eps'
plot 'dp.dat' using 1:3 title 'Average' with linespoints lw 8 ps 4, 'dp.dat' using 1:4 title 'Maximum' with linespoints lw 8 ps 4

reset
unset log
unset label
set xlabel 'Number of dining philosophers'
set xtics (10,20,30,40)
set key left top
#
set ylabel 'CPU time (sec)'
set terminal post eps enhanced "Helvetica" 25
set out 'dp-cpu.eps'
plot 'dp.dat' using 1:5 title 'Average' with linespoints lw 8 ps 4, 'dp.dat' using 1:6 title 'Maximum' with linespoints lw 8 ps 4

reset
unset log
unset label
set key left top
#
set xlabel '% time savings'
set ylabel 'Number of agents'
set xtics (0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1)
set terminal post eps enhanced "Helvetica" 25
set out 'dp-exit.eps'
plot "dp-exit.dat" u 1:2 with boxes title "" lw 8 
