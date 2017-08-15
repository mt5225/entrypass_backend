# entrypass demo

## start server
python app.py
python srv.py

## service ports
- socket server: 8095
- api server : 8096


## query door status
curl -i -X GET http://localhost:9008/doorstatus

## send dummy data
python sender.py DoorClose
python sender.py DoorOpen

