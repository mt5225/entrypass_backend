import socket
import xml.etree.ElementTree as ET
import sqlite3
import sys
import logging
import time

# create logger
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def save_to_db(xmlstring):
    """ str to xml to database """
    docroot = ET.ElementTree(ET.fromstring(xmlstring)).getroot()
    ETYPE = docroot.find('ETYPE').text.strip()
    logging.debug('ETYPE = ' + ETYPE);
    
    if(ETYPE != '0'):
        #logging.debug(xmlstring)
        logging.warn('not a type 0 message, discard')
        return
    
    TRCODE = docroot.find('TRCODE').text.strip()
    
    if(TRCODE not in ['Dc', 'Dg']):
        logging.warn('not in Dc or Dg, discard')
        return
	
    logging.debug(xmlstring)
    TRDATE = docroot.find('TRDATE').text.strip()
    TRTIME = docroot.find('TRTIME').text.strip()
    TRDESC = docroot.find('TRDESC').text.strip()
    TRID = docroot.find('STAFFNO').text.strip()
    DEVNAME = docroot.find('DEVNAME').text.strip()
    try:
        conn = sqlite3.connect('./entrypass.db')
        cur = conn.cursor()
        record = (ETYPE, TRDATE, TRTIME, TRCODE, TRDESC, TRID, DEVNAME)
        logging.debug('|'.join(str(e) for e in record))
        cur.execute("INSERT INTO live VALUES(?,?,?,?,?,?,?)", record)
        conn.commit()
    except sqlite3.Error, e:
        print "Error %s:" % e.args[0]
        sys.exit(1)
    finally:
        if conn:
            conn.close()


def recv_timeout(the_socket,timeout=2):
    #make socket non blocking
    the_socket.setblocking(0)
     
    #total data partwise in an array
    total_data=[];
    data='';
     
    #beginning time
    begin=time.time()
    while 1:
        #if you got some data, then break after timeout
        if total_data and time.time()-begin > timeout:
            break
         
        #if you got no data at all, wait a little longer, twice the timeout
        elif time.time()-begin > timeout*2:
            break
         
        #recv something
        try:
            data = the_socket.recv(8192)
            if data:
                total_data.append(data)
                #change the beginning time for measurement
                begin = time.time()
            else:
                #sleep for sometime to indicate a gap
                time.sleep(0.1)
        except:
            pass
     
    #join all parts to make final string
    return ''.join(total_data)

def main():
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind(('0.0.0.0', 9005))
    serversocket.listen(5) # become a server socket, maximum 5 connections

    while True:
        connection, address = serversocket.accept()
        buf = recv_timeout(connection)
        if len(buf) > 0:
            save_to_db(buf)

if __name__ == '__main__':
   main()
