@echo off
start cmd /k "cd backend && python app.py"
timeout /t 5
start cmd /k "cd frontend && streamlit run main.py"
exit
