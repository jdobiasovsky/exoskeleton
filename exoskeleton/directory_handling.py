"""Classes and functions to handle directories, like reading and moving."""

from settings import config
import os
import errno
import shutil


class Document:
    """
    Class representing Documents being processed during workflow. On init 

    Valid directory contains nothing else than files containing following extensions
    as specified in check_redundant_files() -- allowed_extensions = (".tif", ".txt", ".xml")
    Also provides functions to check for two common errors that occur during import:
    missing ocr files & wrong image format which can be performed on instances of class which 
    contain no redundancy.
    """

    def __init__(self, directory_path):
        """Initialize Document class."""

        if os.path.isdir(directory_path) is True:
            self._id = os.path.basename(directory_path)
            self._path = directory_path
            self._contents = os.listdir(directory_path)
        else:
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), directory_path)

        self.status = "initialization"
        self.message = "New document directory is being initialized."


        @property
        def id(self):
            return self._id

        @id.setter
        def id(self, value):
            if os.path.isdir(value) is False:
                raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), value)
            self._id = os.path.basename(value)

        @id.deleter
        def id(self):
            del self._id

        @property
        def path(self):
            return self._path

        @path.setter
        def path(self, value):
            if os.path.isdir(value) is False:
                raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), value)
            self._path = value

        @path.deleter
        def path(self):
            del self._path

        @property
        def contents(self):
            return self._contents

        @contents.setter
        def contents(self, value):
            if os.path.isdir(value) is False:
                raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), value)
            self._contents = value

        @contents.deleter
        def contents(self):
            del self._contents


    def structure_check(self):
        """Check folder for any extra files. Return true if no redundant files are present."""
        # make list of files that don't end with allowed extensions
        allowed_extensions = (".tif", ".txt", ".xml")
        invalid_files = [file for file in self._contents if not file.endswith(allowed_extensions)]
        if len(invalid_files) != 0:
            self.invalid_files = invalid_files
            self.status = "invalid_structure"
            return False

        else:
            return True 

    def verify_ocr(self):
        """
        Check if folder contains valid ocr, return true if it does.
        
        Use only on folders with no redundant files (only contains allowed extensions (see class definition).
        """  
        tif_count = len([file for file in self._contents if file.endswith(".tif")])
        ocr_count = len([file for file in self._contents if file.endswith((".xml", ".txt"))])/2
        
        if ocr_count == 0:
            self.status = "ocr_missing"
            self.message = "No ocr files found."
            
        elif ocr_count != tif_count:
            self.status = "ocr_missing_partial"
            self.message = "Ocr files found, but they don't match the number of images."
        elif ocr_count == tif_count:
            self.status = "ocr_valid"
            


