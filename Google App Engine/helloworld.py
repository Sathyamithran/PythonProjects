import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.responsive.write("Hello World")


app = webapp2.WSGIApplication([('/', MainPage),],debug=True)
