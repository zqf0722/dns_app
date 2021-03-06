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

Make sure to first start running FS and AS before doing registration. The registration function is under FS folder and its name is registration.py. Just modify the body of the json in registration.py and run python registration.py. If you want to register for another DNS, use the registration.py under FS folder, and run it again.

Also, if you want to automatically register. See Dockerfile under US folder. There is a line of code which allows you to do that. If you want to automatically register, remember to start running FS and AS first or it will give the wrong results.
