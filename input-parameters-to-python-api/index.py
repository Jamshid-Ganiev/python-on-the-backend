import tornado.web
import tornado.ioloop

class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("<h1>Hello, World!</h1> <h2>This is a Python Command</h2>")


class queryParamRequestHandler(tornado.web.RequestHandler):
    def get(self):
        num = self.get_argument("num")
        if num.isdigit():
            r = "odd" if int(num) % 2 == 1 else "even"
            self.write(f"<h1 style='color:green;'>The integer {num} is {r}</h1>")
        else:
            self.write(f"<h2>{num} is not a valid integer</h2>")


class resourceParamRequestHandler(tornado.web.RequestHandler):
    def get(self, studentName, courseId):
        self.write(f"<h1>Welcome {studentName}</h1> <h2>The course ID is {courseId}</h2>")


if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", basicRequestHandler),
        (r"/isEven", queryParamRequestHandler),
        # only the uppercase letters in [a-z] section
        (r"/student/([a-z]+)/([0-9]+)", resourceParamRequestHandler),
        

    ])

port = 8882
app.listen(port)
print(f"Application is ready and listening on port:{port}")
tornado.ioloop.IOLoop.current().start()