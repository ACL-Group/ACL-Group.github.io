set size ratio 0.5
aqua = "#00FFFF"; azure = "#F0FFFF";
aliceblue = "#F0F8FF"
set style fill solid 1.00 border 0

set tics font ", 15"
set key font "Helvetica,12"
set xtics font "Helvetica,12"
set xtics font "Helvetica,12"
set key top outside horizontal center
set yrange [0:15]
set xlabel "Different training days" font "Helvetica, 15";
set ylabel "HR Score (%)" font "Helvetica, 15";
#unset tics
set grid ytics
set ytics 0,3,15
set xtics ('9 days' 0, '6 days' 1, '3 days' 2)

#set xtics center offset 0,-1
set style histogram clustered gap 3   #//gap 2表示裂隙宽等于矩形宽度的2倍
set style fill pattern border -1 #//fill solid表示完全填充柱体，后面跟0-1的参数，1表示完全填充，border 表示柱体的边线颜色，-1表示黑色。这里还可以加参数pattern
plot 'data_2.txt' using 1 with histogram ls 2 title 'CBCF', \
'data_2.txt' using 2 with histogram ls 3 title 'STAN', 'data_2.txt' using 3 with histogram ls 3 title ' GRU4Rec', \
'data_2.txt' using 4 with histogram ls 3 title 'SASRec', 'data_2.txt' using 5 with histogram ls 3 title 'SRGNN', \
'data_2.txt' using 6 with histogram ls 3 title 'SGNNHN', 'data_2.txt' using 7 with histogram ls 3 title 'STAMP',\
'data_2.txt' using 8 with histogram ls 3 title ' CAR+P+N'
