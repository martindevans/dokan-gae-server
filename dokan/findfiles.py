from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext import db

import time
import dokan
from dokan import models

class FindHandler(webapp.RequestHandler):
	def get(self):
		folder = models.FindFolder(self.request.get("filename"), False)
		
		out = self.response.out.write
		
		files = models.File.all().filter("parent_folder = ", folder)
		folders = models.Folder.all().filter("parent_folder = ", folder)
	
		out("response_code=" + str(dokan.DOKAN_SUCCESS))
	
		count = 0
		for file in files:
			out("," + str(count) + "=128|"
			+ str(long(time.mktime(file.created.timetuple()))) + "|"
			+ file.filename + "|"
			+ str(long(time.mktime(file.modified.timetuple()))) + "|"
			+ str(long(time.mktime(file.modified.timetuple()))) + "|"
			+ "0")
			count = count + 1
			
		for folder in folders:
			out("," + str(count) + "=16|"
			+ str(long(time.mktime(folder.created.timetuple()))) + "|"
			+ folder.foldername + "|"
			+ str(long(time.mktime(folder.modified.timetuple()))) + "|"
			+ str(long(time.mktime(folder.modified.timetuple()))) + "|"
			+ "0")
			count = count + 1
			
		out(",count=" + str(count) + ",message=find files")

def main():
    application = webapp.WSGIApplication([('/FindFiles.*', FindHandler)],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()