#!/usr/bin/env python3
"""
Simple health check server that runs alongside the main application.
This allows Railway's health checks to succeed while the main Gradio app is starting.
"""

import os
import socket
import threading
import time
from http.server import HTTPServer, BaseHTTPRequestHandler

# Port for the health check server (different from main app)
HEALTH_PORT = int(os.environ.get("HEALTH_PORT", 8080))


class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        """Respond to GET requests with a 200 OK status"""
        if self.path == "/" or self.path == "/health" or self.path == "/healthz":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(b'{"status":"ok"}')
        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(b'{"status":"not found"}')
    
    # Suppress logs for health check requests
    def log_message(self, format, *args):
        return


def wait_for_port(port, host="localhost", timeout=60.0):
    """Wait until a port is open on the given host"""
    start_time = time.time()
    while True:
        try:
            with socket.create_connection((host, port), timeout=1.0):
                return True
        except OSError:
            if time.time() - start_time >= timeout:
                return False
            time.sleep(1.0)


def run_health_server():
    """Run the health check server"""
    print(f"Starting health check server on port {HEALTH_PORT}")
    server = HTTPServer(("0.0.0.0", HEALTH_PORT), HealthHandler)
    server.serve_forever()


if __name__ == "__main__":
    # Start the health check server in a separate thread
    health_thread = threading.Thread(target=run_health_server, daemon=True)
    health_thread.start()
    
    # This can be run standalone for testing
    print("Health check server running. Press Ctrl+C to stop.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping health check server...") 