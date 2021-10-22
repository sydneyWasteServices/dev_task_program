# openpyxl 
# xlwings  => it can directly modify excel 


print("hello world")


# In excel VBA
sub RunPython()
    Dim shell As Object, exePath As String, scriptPath as String

    Set Shell = VBA.CreateObject("Wscript.shell")

    # change , It is three double quote
    exePath = """C:\PythonInstall\37\python.exe"""
    # Path that the script you wrote
    scriptPath = "C:\test\v1\Script_V1.py"

    Dim rangeColA as String, rangeColB As String
    rangeColA = "A1:A5000|SUM"
    rangeColB = "B1:B" & Range("B1").End(xlDown).Row & "|AVG"

    # Excel file path 
    Dim filePath As String
    
    filePath = Application.ActiveWorkbook.FullName
    # Msg Box filePath
    # To get active sheet : Application .ActiveSheet

    #  Mutiple Strings with range + action seperated by ","

    Dim param As String
    param = rangeColA & "," & rangeColB



    # Build command to be executed 
    # exePath installation folder 
    Dim command As String 
    command = exePath & " " & scriptPath & " " filePath & " " & param


import sys
import openpyxl

from openpyxl.utils.cell import(coordinate_to_tuple)





