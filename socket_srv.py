import socket
import xml.etree.ElementTree as ET
import sqlite3
import sys
import logging

# create logger
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def save_to_db(xmlstring):
    """ str to xml to database """
    docroot = ET.ElementTree(ET.fromstring(xmlstring)).getroot()
    ETYPE = docroot.find('ETYPE').text.strip()
    TRDATE = docroot.find('TRDATE').text.strip()
    TRTIME = docroot.find('TRTIME').text.strip()
    TRCODE = docroot.find('TRCODE').text.strip()
    TRDESC = docroot.find('TRDESC').text.strip()
    TRID = docroot.find('TRID').text.strip()
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



def main():
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind(('0.0.0.0', 9005))
    serversocket.listen(5) # become a server socket, maximum 5 connections

    while True:
        connection, address = serversocket.accept()
        buf = connection.recv(1024)
        if len(buf) > 0:
            save_to_db(buf)

if __name__ == '__main__':
   main()
