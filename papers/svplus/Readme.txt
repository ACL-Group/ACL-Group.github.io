
概述
--------

    这是为《中国科技论文在线》投稿所用的TeX模板文件包，主要针对TeX Live 2009/2010系统，基于这些系统自带的ctex宏包而开发。

    本模板包括的文件清单如下：

    csoarticle.cls      《中国科技论文在线》稿件文档类[必需]
    cso-gbk.def         《中国科技论文在线》宏定义文件[GBK编码方式必需]
    cso-utf8.def        《中国科技论文在线》宏定义文件[UTF8编码方式必需]
    csologo.eps         《中国科技论文在线》稿件页眉图片[latex编译方式必需]
    csologo.pdf         《中国科技论文在线》稿件页眉图片[pdflatex编译方式必需]
    csosampleUTF8.tex   稿件示例文件，UTF8编码
    csosampleGBK.tex    稿件示例文件，GBK编码
    figsamp.eps         稿件示例文件，latex编译方式必需
    figsamp.pdf         稿件示例文件，pdflatex编译方式必需
    Readme.txt          本文档


样例文件
--------

    样例文件可以通过以下方式生成PDF结果文件。

    方法一(推荐的首选方法)：

        xelatex csosampleUTF8.tex

    方法二：

        pdflatex csosampleUTF8.tex

    方法三：

        latex csosampleUTF8.tex
        dvipdfmx csosampleUTF8

    方法四：

        pdflatex csosampleGBK.tex

    方法五：

        latex csosampleGBK.tex
        dvipdfmx csosampleGBK


版本历史
--------

    v 0.02
        - 加入对GBK编码的支持
        - 加入对latex/pdflatex编译方式的支持
        - 发行中加入cso-gbk.def和cso-utf8.def两个文件
        - 样例加入eps格式的图片，去除pgf格式的图片
        - 样例中加入数学定理环境的使用
        - 添加宏包amssymb,amsthm的自动加载
        - 修正图表标题上下留白大小
        - 更换页眉logo文字更“瘦”一些，更改了页眉网址的显示字体
        - 调整了页眉与页脚的边距
        - 增加Readme.txt

    v 0.01
        - 支持UTF8编码
        - 支持xelatex编译方式


开发组
--------

    作者：WANG Yong-Xian (yxwang@nudt.edu.cn)
    反馈及建议，请用电子邮件跟作者联系；也可通过《中国科技论文在线》编辑部转达。


致谢
--------

   CTeX社区(www.ctex.org)
   milksea @ CTeX
   水寿松  @ CTeX
