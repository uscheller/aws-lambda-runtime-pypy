function hello () {
  EVENT_DATA=$1
  echo "$EVENT_DATA" 1>&2;
  RESPONSE="Echoing request: '$EVENT_DATA'"

  echo "{\"statusCode\": 200, \"body\": \"yeehaw\"}"
}
