import tornado.web
import tornado.ioloop
import json


class listFruitsRequestHandler(tornado.web.RequestHandler):
    def get(self):
        fh = open("fruits.txt", 'r')
        fruits = fh.read().splitlines()
        fh.close()

        self.write(json.dumps(fruits))

    def post(self):
        fruit = self.get_argument("fruit")
        fh = open("fruits.txt", 'a')
        fh.write(f"\n{fruit}")
        fh.close()

        self.write(json.dumps({"message": "Fruit added successfully."}))


if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/fruit", listFruitsRequestHandler),
    ])

port = 8882
app.listen(port)
print(f"Application is ready and listening on port:{port}")
tornado.ioloop.IOLoop.current().start()