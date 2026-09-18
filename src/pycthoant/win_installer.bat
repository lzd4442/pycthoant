@echo off
chcp 65001 >nul 2>&1
"%~dp0python.exe" "%~dp0pycthoant.py" %*
