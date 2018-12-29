@echo off
set argc=0
for %%i in (%*) do set /A argc+=1

set TARGET=prog.exe
set MAIN_CLASS=FGMain
set BUILD_OBJECTS=src\*.cs src\FGSharp\*.cs
set LIBRARY_OBJECTS=src\FGSharp\Utility\*.cs 
set LIBS=-r:"FGSharp.dll" -r:"C:/Program Files (x86)/Mono/lib/gtk-sharp-2.0/pango-sharp.dll" -r:"C:/Program Files (x86)/Mono/lib/gtk-sharp-2.0/atk-sharp.dll" -r:"C:/Program Files (x86)/Mono/lib/gtk-sharp-2.0/gdk-sharp.dll" -r:"C:/Program Files (x86)/Mono/lib/gtk-sharp-2.0/gtk-sharp.dll" -r:"C:/Program Files (x86)/Mono/lib/gtk-sharp-2.0/glib-sharp.dll"

if %argc% == 0 (
    goto BUILD_MAIN

) 

if %argc% == 1 ( 
    if "%~1" == "clean" goto CLEAN_DIR
    if "%~1" == "client" goto BUILD_CLIENT
    if "%~1" == "lib" goto BUILD_LIBRARY

    echo %~1 is not a valid command.
    echo No action taken.
    goto end
)

:BUILD_MAIN
echo Compiling main.
mcs %LIBS% -out:%TARGET% -t:exe -m:FGMain %BUILD_OBJECTS%

:BUILD_CLIENT
echo Compiling client.
mcs -t:exe -out:client.exe src\client\TCPCli.cs

:BUILD_LIBRARY
mcs -t:library -out:FGSharp.dll %LIBRARY_OBJECTS% 

:CLEAN_DIR
echo Cleaning directory.
del %TARGET% client.exe
goto end

:end