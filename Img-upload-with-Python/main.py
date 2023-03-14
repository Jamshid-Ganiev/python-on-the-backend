import tornado.web
import tornado.ioloop


class uploadImageHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

    def post(self):
        files = self.request.files["imgFile"]
        for f in files:
            fh = open(f"upload/{f.filename}", 'wb')
            fh.write(f.body)
            fh.close()
        self.write(f"<a href='http://localhost:8080/upload/{f.filename}'>See the image you've uploaded</a>")


if (__name__ == "__main__"):
    app = tornado.web.Application([
        (r"/", uploadImageHandler),
        (r"/upload/(.*)", tornado.web.StaticFileHandler, {'path': 'upload'})
    ])

    app.listen(8080)
    print("Listening on port: 8080")

    tornado.ioloop.IOLoop.instance().start()