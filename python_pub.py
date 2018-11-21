import redis
import time


CHANNEL_NAME = "kanal1"


def connect(host, port):
    return redis.Redis(host=host, port=port)


def pub(host, port, channel):
    r = connect(host, port)

    for i in range(0, 11):
        print("Publishing message to " + channel)
        message = "zprava #{}".format(i)
        r.publish(channel, message)

        time.sleep(1)


pub("127.0.0.1", 6379, CHANNEL_NAME)
