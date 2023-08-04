import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from views import (
    get_all_metals, get_single_metal, create_metal, delete_metal, update_metal,
    get_all_orders, get_single_order, create_order, delete_order, update_order,
    get_all_sizes, get_single_size, create_size, delete_size, update_size,
    get_all_styles, get_single_style, create_style, delete_style, update_style
)

class HandleRequests(BaseHTTPRequestHandler):
    """Controls the functionality of any GET, PUT, POST, DELETE requests to the server"""
    def parse_url(self, path):
        path_params = path.split("/")
        resource = path_params[1]
        id = None

        try:
            id = int(path_params[2])
        except IndexError:
            pass
        except ValueError:
            pass

        return (resource, id)

    def do_GET(self):
        """Handles GET requests to the server """
        self._set_headers(200)

        response = {}  # Default response

        # Parse the URL and capture the tuple that is returned
        (resource, id) = self.parse_url(self.path)

        if resource == "metals":
            if id is not None:
                response = get_single_metal(id)
            else:
                response = get_all_metals()
        elif resource == "orders":
            if id is not None:
                response = get_single_order(id)
            else:
                response = get_all_orders()
        elif resource == "sizes":
            if id is not None:
                response = get_single_size(id)
            else:
                response = get_all_sizes()
        elif resource == "styles":
            if id is not None:
                response = get_single_style(id)
            else:
                response = get_all_styles()
                
        self.wfile.write(json.dumps(response).encode())

    def do_POST(self):
        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)

        # Convert JSON string to a Python dictionary
        post_body = json.loads(post_body)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

    # Initialize new resource variables
        new_resource = None

        if resource == "metals":
            new_resource = create_metal(post_body)
        if resource == "orders":
            new_resource = create_order(post_body)
        if resource == "sizes":
            new_resource = create_size(post_body)
        if resource == "styles":
            new_resource = create_style(post_body)

        self.wfile.write(json.dumps(new_resource).encode())
        
    def do_DELETE(self):
        # Set a 204 response code
        self._set_headers(204)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        # Delete a single animal from the list
        if resource == "metals":
            delete_metal(id)
        if resource == "orders":
            delete_order(id)
        if resource == "sizes":
            delete_size(id)
        if resource == "styles":
            delete_style(id)
            
        self.wfile.write("".encode())

    # def do_PUT(self):
    #     """Handles PUT requests to the server"""
    #     self.do_POST()
    def do_PUT(self):
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)
    
        success = False
        
        # Delete a single animal from the list
        if resource == "orders":
            success = update_order(id, post_body)
        if resource == "metals":
            success = update_metal(id, post_body)

        if success:
            self._set_headers(204)
        else:
            self._set_headers(404)
    # Encode the new order and send in response
        self.wfile.write("".encode())

    def _set_headers(self, status):
        """Sets the status code, Content-Type, and Access-Control-Allow-Origin headers on the response.

        Args:
            status (number): The status code to return to the front end.
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_OPTIONS(self):
        """Sets the options headers"""
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers', 'X-Requested-With, Content-Type, Accept')
        self.end_headers()

# Entry point of this application.
def main():
    """Starts the server on port 8088 using the HandleRequests class"""
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()

if __name__ == "__main__":
    main()
