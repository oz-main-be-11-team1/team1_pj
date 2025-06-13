#!/bin/bash

echo "==== Restarting Nginx ===="
echo

# Nginx 설정 테스트 및 재시작
sudo nginx -t
if [ $? -eq 0 ]; then
    sudo systemctl restart nginx
    echo "Nginx restarted successfully."
else
    echo "Nginx configuration test failed. Please fix the errors."
    exit 1
fi

echo "==== Launching Flask app ===="
echo

# 가상환경 활성화
if [ -f ".venv/bin/activate" ]; then
    source .venv/bin/activate
else
    echo "Virtual environment not found. Please ensure '.venv' exists."
    exit 1
fi

# Gunicorn 실행
gunicorn --workers 4 --bind 127.0.0.1:8000 wsgi:app --daemon --log-file gunicorn.log

if [ $? -eq 0 ]; then
    echo "Flask app launched successfully with Gunicorn."
    echo

    sudo lsof -i :8000
    echo

    echo "Logs can be found in gunicorn.log."
    echo

    echo "==== To stop the Flask app ===="
    echo

    echo "To stop the Flask app, you can run the following command:"
    echo "Run the 'terminate.sh' script to stop the Flask app."
else
    echo "Failed to launch Flask app with Gunicorn."
    exit 1
fi