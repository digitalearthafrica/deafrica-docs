@ECHO OFF
SETLOCAL

PUSHD "%~dp0"

REM Command file for building the Digital Earth Africa Sphinx documentation.

IF "%SPHINXBUILD%"=="" (
    SET "SPHINXBUILD=sphinx-build"
)

SET "SOURCEDIR=."
SET "BUILDDIR=_build"

IF "%~1"=="" GOTO help

REM Confirm that Sphinx is installed and available.
%SPHINXBUILD% --version >NUL 2>NUL

IF ERRORLEVEL 1 (
    ECHO.
    ECHO The sphinx-build command was not found.
    ECHO.
    ECHO Install the documentation requirements with:
    ECHO     python -m pip install -r requirements.txt
    ECHO.
    ECHO You may also set the SPHINXBUILD environment variable to the
    ECHO full path of the sphinx-build executable.
    ECHO.
    GOTO error
)

REM Optional command: make.bat cleanall
IF /I "%~1"=="cleanall" (
    ECHO Removing the complete build directory...
    IF EXIST "%BUILDDIR%" RMDIR /S /Q "%BUILDDIR%"

    IF ERRORLEVEL 1 GOTO error

    ECHO Build directory removed successfully.
    GOTO end
)

REM Build the requested Sphinx target, for example:
REM     make.bat html
REM     make.bat clean
REM     make.bat linkcheck
%SPHINXBUILD% -M "%~1" "%SOURCEDIR%" "%BUILDDIR%" %SPHINXOPTS% %O%

IF ERRORLEVEL 1 GOTO error

GOTO end

:help
%SPHINXBUILD% -M help "%SOURCEDIR%" "%BUILDDIR%" %SPHINXOPTS% %O%
GOTO end

:error
ECHO.
ECHO The documentation build failed.
POPD
ENDLOCAL
EXIT /B 1

:end
POPD
ENDLOCAL
EXIT /B 0