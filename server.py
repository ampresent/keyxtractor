#!/usr/bin/env python2
import SocketServer
import BaseHTTPServer
import SimpleHTTPServer
import sys
import extractor
import logging
import pdb

keyxtractor = extractor.Extractor()

class MyHTTPServer(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_POST(self, *args):
        try:
            length = int(self.headers.getheader('content-length'))
            query = self.rfile.read(length)
            logging.debug('Received: {}...'.format(query))
            
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()

            response = keyxtractor.extract(query, top=15)
            self.wfile.write('\n'.join(response))
        except:
            self.send_response(500)
            logging.error('Failed to extract keyword.')


PORT = 27896
if len(sys.argv) > 1:
    PORT = int(sys.argv[1])

logging.info('Running at localhost:{}'.format(PORT))

server_address = ('127.0.0.1', PORT)
httpd = SocketServer.TCPServer(("", PORT), MyHTTPServer)

sa = httpd.socket.getsockname()
logging.info('Connection from {}'.format(sa))

httpd.serve_forever()
