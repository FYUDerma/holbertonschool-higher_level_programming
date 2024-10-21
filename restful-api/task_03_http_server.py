#!/usr/bin/python3
import http.server
import socketserver
import json

PORT = 8000


class BasicHttpServer(http.server.BaseHTTPRequestHandler):
    def root(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(b"Hello, this is a simple API!")
    def data(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        data = {
            "name": "John",
            "age": 30,
            "city": "New York"
        }
        self.wfile.write(json.dumps(data).encode('utf-8'))
    def status(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"OK")
    def info(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        data = {
            "version": "1.0",
            "description": "A simple API built with http.server"
        }
        self.wfile.write(json.dumps(data).encode('utf-8'))
    def non_root(self):
        self.send_response(404)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Endpoint not found")
    def do_GET(self):
        path = {
            "/": self.root,
            "/data": self.data,
            "/status": self.status,
            "/info": self.info
        }
        path.get(self.path, self.non_root)()


if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), BasicHttpServer) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()
