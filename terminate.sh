#!/bin/bash

echo "==== Stopping Flask app ===="
echo

# Gunicorn 프로세스 ID 확인 후 종료 (모든 워커 포함)
PIDS=$(ps aux | grep 'gunicorn' | grep -v 'grep' | awk '{print $2}')
if [ -n "$PIDS" ]; then
    echo "Killing the following PIDs:"
    # 각 PID를 한 줄씩 출력
    for PID in $PIDS; do
        sudo kill $PID
        echo "Killed PID: $PID"
    done
else
    echo "No Gunicorn process found."
fi