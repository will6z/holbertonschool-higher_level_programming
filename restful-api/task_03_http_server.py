#!/usr/bin/python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        routes = {
            '/': self.handle_root,
            '/data': self.handle_data,
            '/status': self.handle_status
        }

        handler = routes.get(self.path, self.handle_not_found)
        handler()

    def handle_root(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"Hello, this is a simple API!")

    def handle_data(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        response = {"name": "John", "age": 30, "city": "New York"}
        self.wfile.write(json.dumps(response).encode())

    def handle_status(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"OK")

    def handle_not_found(self):
        self.send_response(404)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"Endpoint not found")


def run_server():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MyHTTPRequestHandler)
    print('Starting server on port 8000...')
    httpd.serve_forever()


if __name__ == "__main__":
    run_server()

