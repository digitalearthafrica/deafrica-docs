@ECHO OFF
SETLOCAL EnableExtensions

PUSHD "%~dp0"

REM ============================================================
REM Digital Earth Africa Sphinx documentation build script
REM ============================================================

IF "%SPHINXBUILD%"=="" SET "SPHINXBUILD=sphinx-build"
IF "%PYTHON%"=="" SET "PYTHON=python"

SET "SOURCEDIR=."
SET "BUILDDIR=_build"
SET "NOTEBOOK_REPO=https://github.com/digitalearthafrica/deafrica-sandbox-notebooks.git"
SET "NOTEBOOK_DIR=sandbox\notebooks"
SET "TOOLS_DIR=%NOTEBOOK_DIR%\Tools"

IF "%~1"=="" GOTO help

REM Commands that do not require Sphinx can run before the Sphinx check.
IF /I "%~1"=="install-docs" GOTO install_docs
IF /I "%~1"=="fetchnotebooks" GOTO fetch_notebooks
IF /I "%~1"=="buildtools" GOTO build_tools
IF /I "%~1"=="fetchtranslation" GOTO fetch_translation
IF /I "%~1"=="cleanall" GOTO clean_all

REM Confirm that Sphinx is installed.
%SPHINXBUILD% --version >NUL 2>NUL

IF ERRORLEVEL 1 (
    ECHO.
    ECHO The sphinx-build command was not found.
    ECHO.
    ECHO Install the documentation requirements with:
    ECHO     make.bat install-docs
    ECHO.
    ECHO Or run:
    ECHO     %PYTHON% -m pip install -r requirements.txt
    ECHO.
    GOTO error
)

IF /I "%~1"=="gettext" GOTO gettext
IF /I "%~1"=="translations" GOTO translations
IF /I "%~1"=="html-fr" GOTO html_fr

REM Pass standard targets to Sphinx, for example:
REM     make.bat html
REM     make.bat clean
REM     make.bat linkcheck
REM     make.bat spelling

%SPHINXBUILD% -M "%~1" "%SOURCEDIR%" "%BUILDDIR%" %SPHINXOPTS% %O%

IF ERRORLEVEL 1 GOTO error
GOTO success


:install_docs
ECHO.
ECHO Installing documentation dependencies...
%PYTHON% -m pip install --upgrade pip

IF ERRORLEVEL 1 GOTO error

%PYTHON% -m pip install -r requirements.txt

IF ERRORLEVEL 1 GOTO error

ECHO Documentation dependencies installed successfully.
GOTO success


:fetch_notebooks
ECHO.

IF NOT EXIST "%NOTEBOOK_DIR%\.git" (
    ECHO Cloning DE Africa Sandbox notebooks...

    IF NOT EXIST "sandbox" MKDIR "sandbox"

    git clone ^
        --depth 1 ^
        --branch main ^
        "%NOTEBOOK_REPO%" ^
        "%NOTEBOOK_DIR%"

    IF ERRORLEVEL 1 GOTO error
) ELSE (
    ECHO Updating DE Africa Sandbox notebooks...

    git -C "%NOTEBOOK_DIR%" fetch --depth 1 origin main
    IF ERRORLEVEL 1 GOTO error

    git -C "%NOTEBOOK_DIR%" reset --hard origin/main
    IF ERRORLEVEL 1 GOTO error

    git -C "%NOTEBOOK_DIR%" clean -fd
    IF ERRORLEVEL 1 GOTO error
)

ECHO Sandbox notebooks are up to date.
GOTO success


:build_tools
CALL :run_fetch_notebooks
IF ERRORLEVEL 1 GOTO error

IF NOT EXIST "%TOOLS_DIR%" (
    ECHO.
    ECHO Notebook tools directory was not found:
    ECHO     %TOOLS_DIR%
    GOTO error
)

ECHO.
ECHO Installing notebook tools...

%PYTHON% -m pip install ^
    --no-dependencies ^
    --disable-pip-version-check ^
    "%TOOLS_DIR%"

IF ERRORLEVEL 1 GOTO error

ECHO Notebook tools installed successfully.
GOTO success


:fetch_translation
IF "%POEDITOR_API_TOKEN%"=="" (
    ECHO.
    ECHO POEDITOR_API_TOKEN is not configured.
    ECHO.
    ECHO Set it before running this command:
    ECHO     SET POEDITOR_API_TOKEN=your-token
    ECHO.
    GOTO error
)

IF "%POEDITOR_PROJECT_ID%"=="" (
    ECHO.
    ECHO POEDITOR_PROJECT_ID is not configured.
    ECHO.
    ECHO Set it before running this command:
    ECHO     SET POEDITOR_PROJECT_ID=your-project-id
    ECHO.
    GOTO error
)

ECHO.
ECHO Downloading translations from POEditor...

%PYTHON% download_translations.py

IF ERRORLEVEL 1 GOTO error

ECHO Translation files downloaded successfully.
GOTO success


:gettext
ECHO.
ECHO Generating gettext translation templates...

IF EXIST "%BUILDDIR%\gettext" (
    RMDIR /S /Q "%BUILDDIR%\gettext"
)

%SPHINXBUILD% ^
    -E ^
    -a ^
    -T ^
    -b gettext ^
    "%SOURCEDIR%" ^
    "%BUILDDIR%\gettext" ^
    %SPHINXOPTS%

IF ERRORLEVEL 1 GOTO error

ECHO Gettext catalogues generated successfully.
GOTO success


:translations
CALL :run_fetch_translation
IF ERRORLEVEL 1 GOTO error

ECHO.
ECHO Compiling translation catalogues...

%PYTHON% -m sphinx_intl build --locale-dir locales

IF ERRORLEVEL 1 GOTO error

ECHO Translation catalogues compiled successfully.
GOTO success


:html_fr
CALL :run_fetch_translation
IF ERRORLEVEL 1 GOTO error

ECHO.
ECHO Compiling French translation catalogues...

%PYTHON% -m sphinx_intl build --locale-dir locales

IF ERRORLEVEL 1 GOTO error

ECHO.
ECHO Building French documentation...

%SPHINXBUILD% ^
    -E ^
    -a ^
    -T ^
    -b html ^
    -D language=fr ^
    -D locale_dirs=locales ^
    "%SOURCEDIR%" ^
    "%BUILDDIR%\html\fr" ^
    %SPHINXOPTS%

IF ERRORLEVEL 1 GOTO error

ECHO.
ECHO French documentation built successfully:
ECHO     %BUILDDIR%\html\fr\index.html
GOTO success


:clean_all
ECHO.
ECHO Removing the complete build directory...

IF EXIST "%BUILDDIR%" (
    RMDIR /S /Q "%BUILDDIR%"
)

IF ERRORLEVEL 1 GOTO error

ECHO Build directory removed successfully.
GOTO success


:run_fetch_notebooks
IF NOT EXIST "%NOTEBOOK_DIR%\.git" (
    ECHO Cloning DE Africa Sandbox notebooks...

    IF NOT EXIST "sandbox" MKDIR "sandbox"

    git clone ^
        --depth 1 ^
        --branch main ^
        "%NOTEBOOK_REPO%" ^
        "%NOTEBOOK_DIR%"

    EXIT /B %ERRORLEVEL%
)

ECHO Updating DE Africa Sandbox notebooks...

git -C "%NOTEBOOK_DIR%" fetch --depth 1 origin main
IF ERRORLEVEL 1 EXIT /B 1

git -C "%NOTEBOOK_DIR%" reset --hard origin/main
IF ERRORLEVEL 1 EXIT /B 1

git -C "%NOTEBOOK_DIR%" clean -fd
EXIT /B %ERRORLEVEL%


:run_fetch_translation
IF "%POEDITOR_API_TOKEN%"=="" (
    ECHO POEDITOR_API_TOKEN is not configured.
    EXIT /B 1
)

IF "%POEDITOR_PROJECT_ID%"=="" (
    ECHO POEDITOR_PROJECT_ID is not configured.
    EXIT /B 1
)

%PYTHON% download_translations.py
EXIT /B %ERRORLEVEL%


:help
ECHO.
ECHO Digital Earth Africa documentation commands
ECHO.
ECHO Standard Sphinx targets:
ECHO     make.bat html
ECHO     make.bat clean
ECHO     make.bat linkcheck
ECHO     make.bat spelling
ECHO.
ECHO Project commands:
ECHO     make.bat install-docs
ECHO         Install documentation dependencies.
ECHO.
ECHO     make.bat fetchnotebooks
ECHO         Clone or update the Sandbox notebooks.
ECHO.
ECHO     make.bat buildtools
ECHO         Fetch notebooks and install notebook tools.
ECHO.
ECHO     make.bat fetchtranslation
ECHO         Download translation files from POEditor.
ECHO.
ECHO     make.bat gettext
ECHO         Generate Sphinx POT translation templates.
ECHO.
ECHO     make.bat translations
ECHO         Download and compile translation files.
ECHO.
ECHO     make.bat html-fr
ECHO         Download translations and build the French site.
ECHO.
ECHO     make.bat cleanall
ECHO         Remove the complete build directory.
ECHO.
GOTO end


:error
ECHO.
ECHO The requested documentation command failed.
POPD
ENDLOCAL
EXIT /B 1


:success
ECHO.
POPD
ENDLOCAL
EXIT /B 0


:end
POPD
ENDLOCAL
EXIT /B 0