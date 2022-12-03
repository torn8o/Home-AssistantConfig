if [ $motion_file != "" ]; then
  body='{"payload": "{\"camera\":\"living room\",\"date\":'"\\\"`date +%x`\\\""',\"time\":'"\\\"`date +%I:%M%p`\\\""'}", "topic": "MOTION TOPIC", "qos": 0, "retain": 0}'
  body_len=$(echo -n "$body" | wc -c)
  head="POST /api/services/mqtt/publish HTTP/1.0\r\nHost: tornha.duckdns.org\r\nUser-Agent: curl/7.47.0\r\nAccept: */*\r\nx-ha-access: a10281028\r\nContent-Type: application/json\r\nContent-Length: ${body_len}\r\n\r\n${body}"
  echo -ne $head | nc -i 5 tornha.duckdns.org
fi
