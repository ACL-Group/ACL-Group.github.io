%%% csoarticle.cls
%%% document class for www.paper.edu.cn
%%% author: WANG Yong-Xian (yxwang@nudt.edu.cn)
%%% 

\NeedsTeXFormat{LaTeX2e}[1995/12/01]
\ProvidesClass{csoarticle}
  [2010/09/27 v0.02 csoarticle
   document class]

% encoding
\newif\ifCSO@GBK \CSO@GBKfalse
\DeclareOption{GBK}{\CSO@GBKtrue\PassOptionsToClass{\CurrentOption}{ctexart}}
\DeclareOption{UTF8}{\CSO@GBKfalse\PassOptionsToClass{\CurrentOption}{ctexart}}
\DeclareOption{gbk}{\CSO@GBKtrue\PassOptionsToClass{\CurrentOption}{ctexart}}
\DeclareOption{utf8}{\CSO@GBKfalse\PassOptionsToClass{\CurrentOption}{ctexart}}

\DeclareOption*{\PassOptionsToClass{\CurrentOption}{ctexart}}
\ExecuteOptions{winfonts,fancyhdr,hyperref}
\ProcessOptions
\LoadClass{ctexart}

\RequirePackage[hmargin=31.7mm,vmargin=31.7mm,headheight=15mm]{geometry}
\RequirePackage{graphicx}
\RequirePackage{amsmath,amssymb,amsthm}


\newcommand\affil[1]{\textsuperscript{#1}}

\newcommand\cso@titleCHN\relax
\newcommand\cso@titleENG\relax
\newcommand\cso@authorCHN\relax
\newcommand\cso@authorENG\relax
\newcommand\cso@affiliationCHN\relax
\newcommand\cso@affiliationENG\relax
\newcommand\cso@cateidCHN\relax
\newcommand\cso@abstractCHN\relax
\newcommand\cso@abstractENG\relax
\newcommand\cso@keywordCHN\relax
\newcommand\cso@keywordENG\relax
\newcommand\cso@authorIntroduction\relax
\newcommand\cso@fund\relax

\newcommand\titleCHN[1]{\renewcommand\cso@titleCHN{#1}}
\newcommand\titleENG[1]{\renewcommand\cso@titleENG{#1}}
\newcommand\authorCHN[1]{\renewcommand\cso@authorCHN{#1}}
\newcommand\authorENG[1]{\renewcommand\cso@authorENG{#1}}
\newcommand\affiliationCHN[1]{\renewcommand\cso@affiliationCHN{#1}}
\newcommand\affiliationENG[1]{\renewcommand\cso@affiliationENG{#1}}
\newcommand\abstractCHN[1]{\renewcommand\cso@abstractCHN{#1}}
\newcommand\abstractENG[1]{\renewcommand\cso@abstractENG{#1}}
\newcommand\keywordCHN[1]{\renewcommand\cso@keywordCHN{#1}}
\newcommand\keywordENG[1]{\renewcommand\cso@keywordENG{#1}}
\newcommand\cateidCHN[1]{\renewcommand\cso@cateidCHN{#1}}
\newcommand\authorIntroduction[1]{\renewcommand\cso@authorIntroduction{#1}}
\newcommand\fund[1]{\renewcommand\cso@fund{#1}}

\ifCSO@GBK
  \input{cso-gbk.def}
\else
  \input{cso-utf8.def}
\fi


\AtBeginDocument{\setcounter{footnote}{0}%
				 \setcounter{section}{-1}}
\AtEndDocument{\clearpage}

%%% 定义页眉页脚
\newsavebox{\csologo}
\sbox{\csologo}{\includegraphics{csologo}}
\RequirePackage{fancyhdr}
\pagestyle{fancy}
\fancyhead{}
\fancyhead[L]{\raisebox{-1.2mm}{\resizebox{45mm}{!}{\usebox{\csologo}}}}
\fancyhead[R]{\zihao{-5}\rm http://www.paper.edu.cn}
\fancyfoot{}
\fancyfoot[C]{-\ {\thepage}\ -}

%%% 定义上标形式的文献引用
\newcommand{\upcite}[1]{\textsuperscript{\cite{#1}}}

%%% 设置列表环境的距离
\setlength{\parsep}{0cm}

%%% 设置图表标题上下空白
\setlength{\abovecaptionskip}{5pt plus 5pt minus 0pt}% 
\setlength{\belowcaptionskip}{5pt plus 5pt minus 0pt}% 


\endinput
