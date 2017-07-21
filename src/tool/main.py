from tool.messages.messages_pb2 import Command


class Tool(object):
    def __init__(self):
        print "Tool running!"

    def run(self):
        c = Command()
        c.temp = True
        print c