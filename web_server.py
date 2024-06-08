from http.server import HTTPServer, BaseHTTPRequestHandler


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def go_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello, World!")


httpd = HTTPServer(('localhost',8000), SimpleHTTPRequestHandler)
print("Serving on port 8000...")
httpd.serve_forever()