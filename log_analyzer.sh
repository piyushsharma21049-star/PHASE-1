#!/bin/bash

LOG="/var/log/auth.log"

echo "======================================"
echo "        LINUX LOG ANALYZER"
echo "======================================"

# Check if log file exists
if [ ! -f "$LOG" ]; then
    echo "Error: $LOG not found."
    echo "Your system may use /var/log/secure instead."
    exit 1
fi

echo
echo "Log File: $LOG"

echo
echo "1. Total Failed Login Attempts"
echo "--------------------------------"
grep -i "failed" "$LOG" | wc -l

echo
echo "2. Total Successful Login Attempts"
echo "-----------------------------------"
grep -i "accepted" "$LOG" | wc -l

echo
echo "3. Failed Login Details"
echo "-----------------------"
grep -i "failed" "$LOG" | tail -10

echo
echo "4. Top IP Addresses for Failed Logins"
echo "-------------------------------------"
grep -i "failed" "$LOG" \
| grep -oE '([0-9]{1,3}\.){3}[0-9]{1,3}' \
| sort \
| uniq -c \
| sort -nr \
| head -10

echo
echo "5. Top Usernames in Failed Logins"
echo "---------------------------------"
grep -i "failed" "$LOG" \
| grep -oE 'invalid user [a-zA-Z0-9._-]+' \
| sort \
| uniq -c \
| sort -nr \
| head -10

echo
echo "======================================"
echo "        ANALYSIS COMPLETED"
echo "======================================"
