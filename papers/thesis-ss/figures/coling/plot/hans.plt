reset
set terminal pngcairo size 900,500 enhanced font 'Verdana,15'
set datafile separator whitespace

set style fill solid border -1
set boxwidth 0.3 absolute
unset xtics

set key outside
set key outside font ",12"
set ytics font ",15"
set ylabel "Accuracy (%)" rotate


array ColorArray[10] = ["#1f77b4", "#ff7f0e", "#2ca02c", "#2ca02c", "#2ca02c", "#2ca02c", "#9467bd", "#9467bd", "#9467bd", "#9467bd"]

# 你可以为模式设置线宽，例如2
lwPattern = 2

# 填充样式数组 - 这里使用整数来表示pattern的类型
array FillStyleArray[10] = [1, 1, 7, 3, 2, 9, 7, 3,2, 9]

array Categories[7] = ["Entailed_Lexi", "Entailed_Subs", "Entailed_Cons", "Non-Entailed_Lexi", "Non-Entailed_Subs", "Non-Entailed_Cons", "Overall"]

do for [j=1:7] {
    # Print the current line being processed
    print "Processing line: ", j, " Category: ", Categories[j]
    set yrange [0:100]
    set output sprintf("hans_roberta_%s.png", Categories[j])
    #set output sprintf("stress_bert_%s.png", Categories[j])
    
    # Fetch the original value and compute maximum value for setting yrange
    stats 'hans_roberta.dat' using 2 every ::j::j nooutput
    original_val = STATS_mean

    max_val = original_val * 1.1
    do for [i=2:11] {
    stats 'hans_roberta.dat' every ::(j)::(j) using i nooutput
    if (STATS_max > max_val) {
        max_val = STATS_max * 1.1
        }
    }
    print "Processing line: ", j, " Category: ", Categories[j],max_val
    set yrange [0:max_val]

    set xrange [0:5.5]

    # 设置线宽和箱宽
    lineWidthPattern = 3   # 虚线的线宽
    boxWidthValue = 0.3    # 箱子的宽度

    set boxwidth boxWidthValue

    # 绘制箱形图，前两列使用 solid 填充，后面的列使用 pattern 填充
    plot for [i=2:3] 'hans_roberta.dat' u ((i-1)*0.5):i every ::(j-1)::(j-1) w boxes title columnheader(i) lc rgb ColorArray[i-1] fillstyle solid noborder,\
    for [i=4:11] 'hans_roberta.dat' u ((i-1)*0.5):i every ::(j-1)::(j-1) w boxes title columnheader(i) lc rgb ColorArray[i-1] fillstyle pattern FillStyleArray[i-1] noborder,\
    original_val w lines lc rgb ColorArray[1] dt 5 linewidth lineWidthPattern notitle
}

