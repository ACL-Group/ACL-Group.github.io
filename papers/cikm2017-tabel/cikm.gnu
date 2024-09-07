set term post eps size 3.5,2.63 color colortext font  ',11'
set output "main-result.eps"
set ylabel "Micro Acc." 
set xlabel "Candidate Size" 
plot "draw.txt" using 2 w lp pt 3 lt 2 lw 2 title "{TextEL}", "draw.txt" using 3 w lp pt 4 lt 4 lw 2 title "{TabEL_B}", "draw.txt" using 4 w lp pt 2 lt 8 lw 2 title "{TabEL_W}", "draw.txt" using 5 w lp pt 6 lt 6 lw 2 title "{Ours}", "draw.txt" using 6 w lp pt 1 lt 1 lw 2 title "{Ours-Full}", "draw.txt" using 7 w lp pt 5 lt 7 lw 2 title "{Upper Bound}"
set key inside bottom left
#set key reverse
set xtics ("1" 0, "3" 1, "5" 2, "10" 3, "20" 4, "30" 5, "40" 6, "50" 7)
set ytics
set yrange [0:0.8]
