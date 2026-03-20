@echo off
cd /d "C:\Users\xxx\Desktop\code claude\pizza-napoli"
git add -A
git commit -m "deploy %date% %time%"
git push origin main
echo.
echo Deploiement termine !
pause
