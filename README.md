# entrypass demo

## start server
python app.py
python srv.py

## service ports
- socket server: 9005
- api server : 9006


## query door status
- curl -i -X GET http://localhost:9006/doorstatus
- curl -i -X GET http://uinnova.com:9006/doorstatus

## send dummy data
- python sender.py DoorClose
- python sender.py DoorOpen

## misc
- the possible port range: 8081 ~ 9010