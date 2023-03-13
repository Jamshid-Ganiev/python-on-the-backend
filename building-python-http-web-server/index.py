import tornado.web
import tornado.ioloop

class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("<h1>Hello, World!</h1> <h2>This is a Python Command</h2>")


class listAnimalsRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("main.html")


if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", basicRequestHandler),
        (r"/animals", listAnimalsRequestHandler),
    ])

port = 8882
app.listen(port)
print(f"Application is ready and listening on port:{port}")
tornado.ioloop.IOLoop.current().start()