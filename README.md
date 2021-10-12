Simplified authoritative server for a network of applications

1. Fibonacci Server (FS) registers its hostname with Authoritative Server (AS).
2. AS creates a DNS record for the FS.
3. AS response the status of the registration.
4. User visit: http://IP_HTTP_SERVER:PORT/fibonacci?hostname=fibonacci.com&number=10&as_ip=IP_AS_SERVER&as_port=PORT_AS_SERVER
5. User Server (US) parse the hostname from the query and query the DNS AS via DNS query
6. AS returns back the IP address of the FS.
7. US request http://IP_FS/fibonacci?number=10
8. FS returns back the answer with 200 code.
9. US returns the result to user.

When you test the program, make sure you change the ip and the as_ip and the url in FS registration function to your own.
Make sure to first start running FS and AS before running US, because I set an automatic DNS registration for FS hostname. If you want to register for another DNS, use the registration.py under US folder, and run it again.
