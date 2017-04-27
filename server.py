from http import server

server_address = ('0.0.0.0' , 8000)
http_handler = server.SimpleHTTPRequestHandler
http_server = server.HTTPServer(server_address, http_handler)

http_server.serve_forever();
