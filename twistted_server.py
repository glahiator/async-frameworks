from twisted.web.resource import Resource
from twisted.internet import reactor
from twisted.web.server import Site


class Greeting(Resource):
    isLeaf = True

    def render_GET(self, request):
        return b"<html>Hello, world!</html>"


root = Resource()
root.putChild(b"hello", Greeting())
reactor.listenTCP(8080, Site(root))
reactor.run()
