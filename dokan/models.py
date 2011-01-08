from google.appengine.ext import db

class Folder(db.Model):
	foldername = db.StringProperty(multiline=False)
	parent_folder = db.SelfReferenceProperty()
	created = db.DateTimeProperty(auto_now_add=True)
	modified = db.DateTimeProperty(auto_now=True)
	
	def getPath(self):
		if self.parent_folder is None:
			return ""
		else:
			return self.parent_folder.getPath() + "\\" + self.foldername

class File(db.Model):
	filename = db.StringProperty(multiline=False)
	parent_folder = db.ReferenceProperty(Folder)
	locked_by = db.IntegerProperty()
	locked = db.BooleanProperty()
	created = db.DateTimeProperty(auto_now_add=True)
	modified = db.DateTimeProperty(auto_now=True)
	
	def getPath(self):
		return self.parent_folder.getPath() + "\\" + self.filename

def FindFilesystemEntry(filepath):
	return None
		
def FindFile(filepath, create=False):
	pathparts = filepath.split('\\')
	if (len(pathparts) == 1):
		root = ["\\"]
		root.extend(pathparts)
		pathparts = root

	file_name = pathparts[-1]
	parentfolderpath = "\\".join(pathparts[0:-1])
	
	folder = FindFolder(parentfolderpath)
	
	if (folder is None):
		return None
		
	if (create):
		return File.get_or_insert(filepath, filename=file_name, parent_folder=folder)
	else:
		return File.all().filter("filename = ", file_name).filter("parent_folder = ", folder).get()
	
def FindFolder(filepath, create=False):
	if (filepath == "\\" or filepath == ""):
		return Folder.get_or_insert("\\", foldername="\\", path="", parent_folder=None)
	
	pathparts = filepath.split('\\')
	
	parentpath = "\\".join(pathparts[0:-1])
	parent = FindFolder(parentpath, False)
	
	if (parent is None):
		return None
	
	if (create):
		return Folder.get_or_insert(parent.getPath() + "\\" + pathparts[-1], foldername=pathparts[-1], parent_folder=parent)
	else:
		return Folder.all().filter("foldername = ", pathparts[-1]).filter("parent_folder = ", parent).get()
	
	