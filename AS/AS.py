#The code is written by Qifeng Zeng
import socket
skt = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
skt.bind(('',53533))
while True:
    data,addr = skt.recvfrom(1024)
    data = data.decode()
    data = data.split('\n')
    if len(data) == 2:
        flag = 'Query'
    else:
        flag = 'Regist'
    for line in data:
        name, value = line.split('=')
        if name == 'NAME':
            search = value
        if name == 'VALUE':
            ip = value
    if flag == 'Regist':
        newfile = []
        with open('DNS.txt','r') as f:
            dns = f.readlines()
            for line in dns:
                name,value = line.replace('\n','').split('=')
                if name == search:
                    newfile.append(search+'='+ip+'\n')
                else:
                    newfile.append(line+'\n')
        with open('DNS.txt','w') as f:
            f.writelines(newfile)
        rst = b'Finished Registration'
        skt.sendto(rst, addr)
    else:
        with open('DNS.txt','r') as f:
            res = f.readlines()
        for line in res:
            name, value = line.replace('\n','').split('=')
            if name == search:
                ip = value
                break
        ReplyMSG = 'TYPE=A\n'+'NAME='+search+'\n'+'VALUE='+ip+'\n'+'TTL=10'
        skt.sendto(ReplyMSG.encode(), addr)
    #skt.close()