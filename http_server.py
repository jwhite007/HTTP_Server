#! /usr/bin/env python
#
from email.utils import formatdate
import socket
from os.path import isfile, join
from mimetypes import guess_type

# import select


# def HTTP_server(self):

#     server_socket = socket.socket(
#         socket.AF_INET,
#         socket.SOCK_STREAM,
#         socket.IPPROTO_TCP)

#     address = ('127.0.0.1', 50000)
#     server_socket.bind(address)
#     server_socket.listen(1)
#     while True:
#         rcv_request()
#         conn.sendall(rec_message)
#     # select():
#     conn.close()


# def rcv_request(self):

#     while True:
#         conn, addr = server_socket.accept()  # this blocks until a client connects

#         rec_message = conn.recv(32)

#     return message


# def parse_request(message):
#     check method for GET
#         if bad raise exception
#     catch bad method
#         build 405
#         return to client
#     check for submission type (directory or file)
#     if directory:
#         show tree

# def lookup():
# map URI onto filesystem (get type and byte number?)
#             if missing:
#                 raise exception
#             if file:
#                 read it
#                 determine type
#                 build a 200 response
#                 return to client
#             if folder:
#                 use os to list directory
#                 build string using utf-8 encoding to send back
#                 build a 200 response
#                 return to client


# def build_response(relative_uri):

#     if relative_uri.endswith('/'):
#         return relative_uri + " is a directory"
#     else:
#         if isfile(join(path, relative_uri)):
#             return relative_uri + " is a file"
#         else:
#             return relative_uri + " is not a file: 404"

def build_response(message, mimetype, code="OK 200"):

    if not isinstance(bytes):
        message = message.encode('utf-8')
    bytelen = len(bytes)
    header_list = []
    status_line = 'HTTP/1.1 ' + code + '\r\n'
    header_list.append(status_line)
    timestamp = 'Date: ' + formatdate(usegmt=True) + '\r\n'
    header_list.append(timestamp)
    server_line = 'Server: Team Python\r\n'
    header_list.append(server_line)
    content_type = 'Content-Type: ' + mimetype + '; char=UTF-8\r\n'
    header_list.append(content_type)
    content_len = 'Content-Length: ' + str(bytelen) + '\r\n'
    header_list.append(content_len)
    header_list.append('\r\n')
    header = '\r\n'.join(header_list)
    return (header, message)

# conn.shutdown(socket.SHUT_RD)
# conn.shutdown(socket.SHUT_WR)
# server_socket.close()

if __name__ == '__main__':
    """Documentaion and tests"""
