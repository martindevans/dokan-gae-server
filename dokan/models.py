from google.appengine.ext import db

class Folder(db.Model):
	foldername = db.StringProperty(multiline=False)
	parent_folder = db.SelfReferenceProperty()
	created = db.DateTimeProperty(auto_now_add=True)
	modified = db.DateTimeProperty(auto_now=True)
	
	def getPath(self):
		if self.parent_folder is None:
			return "\\"
		else:
			return parent_folder.getPath() + "\\" + foldername

class File(db.Model):
	filename = db.StringProperty(multiline=False)
	parent_folder = db.ReferenceProperty(Folder)
	locked_by = db.IntegerProperty()
	locked = db.BooleanProperty()
	created = db.DateTimeProperty(auto_now_add=True)
	modified = db.DateTimeProperty(auto_now=True)
	
	def getPath(self):
		return parent_folder.getPath() + "\\" + filename
	
def FindFile(filepath):
	return None
	
def FindFolder(filepath, create=False):
	if (filepath == "\\" or filepath == ""):
		return Folder.get_or_insert("\\", foldername="\\", path="\\", parent_folder=None)
	
	pathparts = filepath.split('\\')
	
	parentpath = "\\".join(pathparts[0:-1])
	parent = FindFolder(parentpath, False)
	
	if (parent is None):
		return None
	
	if (create):
		return Folder.get_or_insert(parent.getPath() + "\\" + pathparts[-1], foldername=pathparts[-1], parent_folder=parent)
	else:
		return Folder.all().filter("foldername = ", pathparts[-1]).filter("parent_folder = ", parent).get()
	
	