from django.core.files.storage import Storage, FileSystemStorage
from django.conf import settings

class LocalFileStorage(FileSystemStorage):
    pass

class RemoteFileStorage(Storage):
    pass

def select_storage(location=""):
    location = "uploads/"+location
    return LocalFileStorage(location=location) if settings.DEBUG else RemoteFileStorage()

