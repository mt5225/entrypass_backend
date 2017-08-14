import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('localhost', 8095))
str = '''
<?xml version="1.0"?> 
<Event xml:lang="en-US">					
<ETYPE>0</ETYPE> 
<TRDATE>20170810</TRDATE> 
<TRTIME>150110</TRTIME>
 <TRCODE>Dc</TRCODE> 
<TRDESC>Door Open</TRDESC> 
<TRID>012345679AB</TRID>						
</Event> 
'''
clientsocket.send(str)
