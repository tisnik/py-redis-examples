import redis
import time


CHANNEL_NAME = "kanal1"


def connect(host, port):
    return redis.Redis(host=host, port=port)


def handler(message):
    print("type {type}  message '{message}'".format(type=message["type"],
                                                    message=message["data"]))


def sub(host, port, channel):
    r = connect(host, port)
    pubsub = r.pubsub()
    pubsub.subscribe(**{channel: handler})
    while True:
        message = pubsub.get_message()
        if message:
            print(message)
        else:
            time.sleep(1)


sub("127.0.0.1", 6379, CHANNEL_NAME)
