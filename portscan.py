import socket as sc
for port in range (1,1024) :
    try:
        s=sc.socket (sc.AF_INET,sc.SOCK_STREAM)
        s.settimeout (1000)
        s.connect (('10.0.0.1',port))
        print '%d:OPEN' % (port)
        s.close
    except: continue 
