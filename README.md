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

## send dummy data
- python sender.py DoorClose
- python sender.py DoorOpen

## misc
- the possible port range: 8081 ~ 9010