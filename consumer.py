"""this is consumer module to receive message and then save in Mongo """
import json
from kafka import KafkaConsumer
from pymongo import MongoClient

if __name__ == "__main__":
    consumer = KafkaConsumer(
        "test",
        bootstrap_servers='localhost:9092',
        api_version=(0, 11, 5),
        auto_offset_reset='earliest',
        group_id="consumer-group-a")
    print("starting the consumer")

    client = MongoClient(port=27017)
    db = client.profiling_jb_interactive
    my_col = db.message

    for msg in consumer:
        data = json.loads(msg.value)
        print(21,data)
        # save in db
        result = my_col.insert_one(data)
        print(result)
