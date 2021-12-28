from pymongo import MongoClient
import sys
if len(sys.argv) != 3:
    print("specify address and port")
    sys.exit()
    
host = sys.argv[1]
port = int(sys.argv[2])
client = MongoClient(host= host, port = port)
print(client)
print("connect to mongodb successfully")
