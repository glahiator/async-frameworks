from tornado import ioloop, web


class HomeHandler(web.RequestHandler):
    def get(self):
        self.write("Hello, world")


app = web.Application([(r"/", HomeHandler)])
app.listen(8000)
ioloop.IOLoop.instance().start()