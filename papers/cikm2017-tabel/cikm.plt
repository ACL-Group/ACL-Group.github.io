set tics font "Times-Roman, 24"
set ylabel "Micro Acc." font "Times-Roman, 26"
set xlabel "Candidate Size" font "Times-Roman, 26"
plot "draw.txt" using 2 w lw 2 lp pt 3 lt 2 title "{/Times=20 TextEL}", "draw.txt" using 3 w lw 2 lp pt 4 lt 4 title "{/Times=20 TabEL^B}", "draw.txt" using 4 w lp lw 2 pt 2 lt 8 title "{/Times=20 TabEL^W}", "draw.txt" using 5 w lw 2 lp pt 6 lt 6 title "{/Times=20 Ours (Baidu only)}", "draw.txt" using 6 w lw 2 lp pt 1 lt 1 title "{/Times=20 Ours (Full, w/ pre-train)}", "draw.txt" using 7 w lw 2 lp pt 5 lt 7 title "{/Times=20 Upper Bound}"
set key center at 1.5, 0.2
set key reverse
set key Left
set key spacing 1.5
set xtics ("1" 0, "3" 1, "5" 2, "10" 3, "20" 4, "30" 5, "40" 6, "50" 7)
set yrange [0:0.8]
