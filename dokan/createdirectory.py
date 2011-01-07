from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext import db

import dokan
from dokan import models

class CreateHandler(webapp.RequestHandler):
	def get(self):
		filepath = self.request.get("filename")
		
		folder = models.FindFolder(filepath, True)
		
		response = None
		if (folder is None):
			response = dokan.ERROR_PATH_NOT_FOUND
		else:
			response = dokan.DOKAN_SUCCESS
		
		self.response.out.write("response_code=" + str(response) + ",message=" + filepath)

def main():
    application = webapp.WSGIApplication([('/CreateDirectory.*', CreateHandler)],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
