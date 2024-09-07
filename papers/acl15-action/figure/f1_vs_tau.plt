set terminal postscript eps linewidth 2 "Helvetica" 24 enhanced
#set terminal postscript enhanced eps
unset key
set xlabel 'tau'
set ylabel 'Maximum F1'
#set xtics ("0" 0, "0.05" 1, "0.1" 2, "0.15" 3, "0.2" 4, "0.25" 5, "0.3" 6, "0.35" 7, "0.4" 8, "0.45" 9)
set yrange [0.2:1.2]
set xtics 0 ,0.05 ,0.5
#set key inside top right
#set key inside bottom right
set output "f1_vs_tau.eps"
plot 'f1_vs_tau.txt' title 'Verb with 10 concepts' with points lt 1 pt 1 lw 2 ps 2
unset output
set term wxt