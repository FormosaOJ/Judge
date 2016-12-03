#!/usr/bin/env python3
import json

import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.write("Hello, world")

    def post(self):
        # get all argument
        res = {k: self.get_argument(k) for k in self.request.arguments}

        # trans mission and mission result from string to json object.
        res['mission'] = json.loads(res['mission'])
        res['mission_result'] = json.loads(res['mission_result'])

        # print all arguemnt beautifully
        print(json.dumps(res, indent=4, sort_keys=True))


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(12346)
    tornado.ioloop.IOLoop.current().start()
