import os
import webbrowser
import threading
import http.server
import socketserver
import sys

class QuietHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass  # Suppress normal request logs

    def handle_error(self, request, client_address):
        pass  # Suppress other errors

def start_http_server(port=8000):
    directory = os.path.dirname(os.path.abspath(__file__))  # Get current directory
    os.chdir(directory)  # Set as working directory

    server_address = ("", port)

    # Wrap server with try-except to catch and ignore WinError 10053
    class SilentTCPServer(socketserver.ThreadingTCPServer):
        def handle_error(self, request, client_address):
            ex_type, ex_value, _ = sys.exc_info()
            if isinstance(ex_value, ConnectionAbortedError) and ex_value.winerror == 10053:
                return  # Suppress WinError 10053
            super().handle_error(request, client_address)  # Handle other errors normally

    httpd = SilentTCPServer(server_address, QuietHTTPRequestHandler)

    file_to_open = "luaConsole.html"

    # Check if the file exists and set the URL
    if os.path.isfile(os.path.join(directory, file_to_open)):
        url = f"http://localhost:{port}/{file_to_open}"
    else:
        print(f"\033[33mWarning: '{file_to_open}' not found in {directory}. Opening server root instead.\033[0m")
        url = f"http://localhost:{port}/"

    threading.Timer(3, lambda: webbrowser.open(url)).start()

    print(f"\033[32mStarting '{directory}' at {url} (Press Ctrl+C to stop). Please leave this window open for an uninterrupted experience.\033[0m")

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped by user.")
        httpd.server_close()
        os._exit(0)

if __name__ == "__main__":
    start_http_server()