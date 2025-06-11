#!/bin/bash

set -e  # 오류 발생 시 즉시 종료

# 오류 발생 시 오류 메시지를 출력하는 함수
trap 'echo "Error occurred in script at line $LINENO"; exit 1' ERR

echo "==== Install Nginx ===="
echo

# Nginx 설치
sudo yum install nginx -y
echo

echo "==== Modifying form.conf ===="
# EC2 퍼블릭 IP 가져오기
TOKEN=$(curl -s -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600")
PUBLIC_IP=$(curl -s -H "X-aws-ec2-metadata-token: $TOKEN" "http://169.254.169.254/latest/meta-data/public-ipv4")

# 퍼블릭 IP가 없으면 에러 처리
if [ -z "$PUBLIC_IP" ]; then
    echo "Failed to retrieve EC2 public IP. Please check your instance and network settings."
    exit 1
fi

# Nginx 설정 파일 경로
CONF_PATH="form.conf"

# 기존 server_name을 퍼블릭 IP로 변경
if [ -f "$CONF_PATH" ]; then
    sudo sed -i "s/server_name .*/server_name $PUBLIC_IP;/" $CONF_PATH
    echo "Nginx server_name updated to $PUBLIC_IP"
else
    echo "Error: $CONF_PATH does not exist. Exiting."
    exit 1
fi
echo

echo "==== Move form.conf ===="
echo

# form.conf 파일을 이동하기 전에 존재 여부 확인
if [ -f "$CONF_PATH" ]; then
    sudo mv $CONF_PATH /etc/nginx/conf.d/$CONF_PATH
    echo "$CONF_PATH has been moved to /etc/nginx/conf.d/$CONF_PATH"
else
    echo "$CONF_PATH does not exist in the current directory. Exiting."
    exit 1
fi
echo

echo "==== Test and Restart Nginx ===="
echo

# Nginx 설정 파일 테스트
sudo nginx -t
if [ $? -eq 0 ]; then
    echo "Nginx configuration is valid. Restarting Nginx..."
    sudo systemctl restart nginx
else
    echo "Nginx configuration test failed. Please check your form.conf file."
    exit 1
fi

echo
echo "Nginx setup completed successfully!"