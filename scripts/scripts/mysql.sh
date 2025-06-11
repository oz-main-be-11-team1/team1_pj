#!/bin/bash

set -e  # 오류 발생 시 즉시 종료

# 오류 발생 시 오류 메시지를 출력하는 함수
trap 'echo "Error occurred in script at line $LINENO"; exit 1' ERR

echo "==== Install MySQL ===="
echo

# MySQL RPM 다운로드 및 설치
sudo wget https://dev.mysql.com/get/mysql80-community-release-el9-4.noarch.rpm
sudo dnf install mysql80-community-release-el9-4.noarch.rpm -y
sudo dnf install mysql-community-client -y
sudo dnf install mysql-community-server -y

# MySQL 버전 출력
mysql_version=$(mysql -V)
echo
echo -e "MySQL version is: $mysql_version"
echo

# MySQL 실행
sudo systemctl start mysqld

# MySQL 초기 비밀번호 확인 및 저장
sudo grep "temporary password" /var/log/mysqld.log | awk '{print $NF}' > mysql_password.txt
echo "The default MySQL password has been saved to 'mysql_password.txt'."
echo

# 비밀번호 변경 및 스키마 생성 안내
echo -e "\n=== NEXT STEPS ==="
echo "1. Log in to MySQL using the default password:"
echo "   mysql -u root -p"
echo
echo "2. Change the root password using the following SQL command:"
echo "   ALTER USER 'root'@'localhost' IDENTIFIED BY 'NewPsword!12as3';"
echo
echo "3. Create a new schema using the following SQL command:"
echo "   CREATE DATABASE your_schema_name;"
echo
echo "Please replace 'NewPassword!123' and 'your_schema_name' with your desired values."
