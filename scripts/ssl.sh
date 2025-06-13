#!/bin/bash

set -e  # 오류 발생 시 즉시 종료

# 오류 발생 시 오류 메시지를 출력하는 함수
trap 'echo "Error occurred in script at line $LINENO"; exit 1' ERR

echo "==== Create SSL Certificate ===="
echo "==== Generating a Self-Signed SSL Certificate ===="
echo

# EC2 퍼블릭 IP 가져오기
TOKEN=$(curl -s -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600")
PUBLIC_IP=$(curl -s -H "X-aws-ec2-metadata-token: $TOKEN" "http://169.254.169.254/latest/meta-data/public-ipv4")

# 퍼블릭 IP가 없으면 에러 처리
if [ -z "$PUBLIC_IP" ]; then
    echo "Failed to retrieve EC2 public IP. Please check your instance and network settings."
    exit 1
fi

echo
echo "Detected EC2 Public IP: $PUBLIC_IP"
echo

# SSL 디렉토리 생성
sudo mkdir -p /etc/ssl/private
sudo mkdir -p /etc/ssl/certs

# OpenSSL을 위한 기본 정보 설정
COUNTRY="KR"                # 국가 (2글자 코드, 예: KR)
STATE="Seoul"           # 주/도
CITY="Gangnam"             # 도시
ORGANIZATION="OZ"  # 조직 이름
ORG_UNIT="Backend"         # 부서 이름
COMMON_NAME="$PUBLIC_IP"    # 퍼블릭 IP를 CN(Common Name)으로 사용
EMAIL="oz$PUBLIC_IP@oz.comP"    # 이메일 주소

# SSL 인증서 생성 (비대화식)
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
    -keyout /etc/ssl/private/selfsigned.key \
    -out /etc/ssl/certs/selfsigned.crt \
    -subj "/C=$COUNTRY/ST=$STATE/L=$CITY/O=$ORGANIZATION/OU=$ORG_UNIT/CN=$COMMON_NAME/emailAddress=$EMAIL"

echo
echo "==== SSL Certificate Created Successfully ===="
echo "Key: /etc/ssl/private/selfsigned.key"
echo "Certificate: /etc/ssl/certs/selfsigned.crt"