# entrypass demo

## start server
python api_srv.py
python socket_srv.py

## service ports
- socket server: 9005
- api server : 9009


## query door status
- curl -i -X GET http://localhost:9006/doorstatus
- curl -i -X GET http://uinnova.com:9009/doorstatus

## demo steps
- send message
  - click ``Listen`` button
  - python sender.py d01_open
  - python sender.py d02_open
  - python sender.py d01_close
  - python sender.py d02_close
  - click ``reset`` button

- use menu
  - click ``Open D01`` button 
  - click ``Close D01`` button
  - click ``Open D02`` button 
  - click ``Close D02`` button
  - click ``reset`` button

## misc
- the possible port range: 8081 ~ 9010