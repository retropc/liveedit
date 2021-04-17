#!/usr/bin/env python3

import web

MAX_ITEMS = 10
MAX_KEY_SIZE = 20
MAX_DATA_SIZE = 100000

urls = (
  "/", "Index",
  "/data/(.+)", "Data",
)

render = web.template.render("templates/")

class Store:
  def __init__(self, max_items):
    self.max_items = max_items
    self.__d = {}

  def __setitem__(self, key, value):
    if key not in self.__d:
      if len(self.__d) == self.max_items:
        self.__d.pop(next(iter(self.__d)))

    self.__d[key] = value

  def __getitem__(self, key):
    return self.__d.get(key, "")

STORE = Store(max_items=MAX_ITEMS)

class Index:
  def GET(self):
    return render.index()

class Data:
  def GET(self, key):
    verify_key(key)

    web.header("Content-Type", "text/plain;charset=UTF-8")
    return STORE[key]

  def PUT(self, key):
    data = web.data()

    verify_key(key)
    verify_data(data)

    STORE[key] = data

    web.header("Content-Type", "text/plain;charset=UTF-8")
    return "ok"

def verify_key(key):
  if len(key) > MAX_KEY_SIZE:
    raise Exception()

def verify_data(data):
  if len(data) > MAX_DATA_SIZE:
    raise Exception()

app = web.application(urls, globals())

if __name__ == "__main__":
  app.internalerror = web.debugerror
  app.run()

application = app.wsgifunc()
