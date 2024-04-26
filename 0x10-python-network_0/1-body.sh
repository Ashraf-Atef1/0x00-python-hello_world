#!/bin/bash
# Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
#!/bin/bash
# prints the body of the repsonse of requests whose reposnse status is 200.
RESPONSE=$(curl -sI "$1" | grep -E " {1}[0-9]{3} {1}"  | cut -d " " -f 2);if [ $RESPONSE == "200" ]; then curl -sLX GET "$1"; fi
