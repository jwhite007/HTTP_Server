HTTP_Server
===========

This is an implementation of a simple HTTP server.  It does no threading or multiprocessing.

  A socket is created, bound to an address and port, and opened for listening.  The server parses through the request
  header, and then builds and sends an appropriate response (directory listing, file, or proper error repsonse)

I wrote the build-response portion and the appropriate tests.

Contributers:  Matt Dougherty and Luke Petschauer.  Thanks, guys.
