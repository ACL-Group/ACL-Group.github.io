set size ratio 0.5
set tics font "Times, 10"
set xtics font "Times, 15"

set multiplot layout 1,3

unset key

set yrange [0.4:1.2]
set xrange [-1:3]
set ylabel "Accuracy" font "Times, 15";
set xlabel "SNLI" font "Times, 15";
#unset tics
set grid ytics
set ytics 0.4,0.2,1.2
set xtics ('Ent' 0, 'Neut' 1, 'Cont' 2)

set xtics center offset 0,0
set style histogram clustered gap 1  #//gap 2表示裂隙宽等于矩形宽度的2倍
set style fill pattern border -1 #//fill solid表示完全填充柱体，后面跟0-1的参数，1表示完全填充，border 表示柱体的边线颜色，-1表示黑色。这里还可以加参数pattern
plot 'snli.txt' using 1 with histogram ls 1 title 'Rule-based', \
'snli.txt' using 2 with histogram ls 1 title 'BART-large' fs pattern 5, \
'snli.txt' using 3 with histogram ls 2 title 'Ensemble static', \
'snli.txt' using 4 with histogram ls 6 title 'Ensemble dynamic' fs pattern 2


set key font "Times,10"
set key box
set key reverse
set key samplen 1 spacing 1
set key width -1
set key vertical Left
set key at graph 1.5, screen 0.6
#unset key

set yrange [0.2:1]
set xrange [-1:3]
set ylabel "Accuracy" font "Times, 15";
set xlabel "MNLI" font "Times, 15";
#unset tics
set grid ytics
set ytics 0.2,0.2,1
set xtics ('Ent' 0, 'Neut' 1, 'Cont' 2)

set xtics center offset 0,0
set style histogram clustered gap 1 #//gap 2表示裂隙宽等于矩形宽度的2倍
set style fill pattern border -1 #//fill solid表示完全填充柱体，后面跟0-1的参数，1表示完全填充，border 表示柱体的边线颜色，-1表示黑色。这里还可以加参数pattern
plot 'mnli.txt' using 1 with histogram ls 1 title 'Rule-based', \
'mnli.txt' using 2 with histogram ls 1 title 'BART-large' fs pattern 5, \
'mnli.txt' using 3 with histogram ls 2 title 'Ensemble static', \
'mnli.txt' using 4 with histogram ls 6 title 'Ensemble dynamic' fs pattern 2

unset multiplot