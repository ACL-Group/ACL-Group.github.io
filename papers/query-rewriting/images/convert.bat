@echo off

if "%1"=="" goto help

pdf2ps %1.pdf t.ps
ps2epsi t.ps %1.eps

echo Convert Finished
goto exit

:help
echo Usage: convert [figure name]
:exit
