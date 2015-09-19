import os
import shutil

#remove source codes folder, ignor errors.
shutil.rmtree("ACE_wrappers", True)
shutil.unpack_archive("ACE-6.3.0.zip")
shutil.copy("./config.h", "./ACE_wrappers/ace")