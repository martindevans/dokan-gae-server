#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util

import time
import dokan
from dokan import models

class InfoHandler(webapp.RequestHandler):
	def get(self):
		out = self.response.out.write
	
		out("filename=" + self.request.get("filename"))
		
		folder = models.FindFolder(self.request.get("filename"))
		if (folder is not None):
			out(",creation_ticks=" + str(long(time.mktime(folder.created.timetuple()))))
			out(",lastaccess_ticks=" + str(long(time.mktime(folder.modified.timetuple()))))
			out(",lastwrite_ticks=" + str(long(time.mktime(folder.modified.timetuple()))))
			out(",length=0")
			out(",attributes=16")
			out(",message=folder")
			out(",response_code=" + str(dokan.DOKAN_SUCCESS))
			return
		
		file = models.FindFile(self.request.get("filename"))
		if (file is not None):
			out(",creation_ticks=" + str(long(time.mktime(file.created.timetuple()))))
			out(",lastaccess_ticks=" + str(long(time.mktime(file.modified.timetuple()))))
			out(",lastwrite_ticks=" + str(long(time.mktime(file.modified.timetuple()))))
			out(",length=0")
			out(",attributes=128")
			out(",message=file")
			out(",response_code=" + str(dokan.DOKAN_SUCCESS))
			return
			
		self.response.out.write("message=not found,response_code=" + str(dokan.ERROR_FILE_NOT_FOUND))

def main():
    application = webapp.WSGIApplication([('/FileInfo.*', InfoHandler)],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
