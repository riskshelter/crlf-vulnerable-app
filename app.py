import urllib.parse
from http.server import BaseHTTPRequestHandler, HTTPServer

class VulnerableHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        query_params = urllib.parse.parse_qs(parsed_path.query)

        if 'user' in query_params:
            user = query_params['user'][0] 
        else:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"Missing 'user' parameter")
            return

        self.send_response(200)
        # not sanitazing user before sending
        self.send_header('Set-Cookie', f'name={user}; Path=/')
        self.end_headers()

        self.wfile.write(f"Hello, {user}!".encode('utf-8'))

def run(server_class=HTTPServer, handler_class=VulnerableHTTPRequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting vulnerable server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
