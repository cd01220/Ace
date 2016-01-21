import os
import shutil

#remove source codes folder, ignor errors.
if os.path.exists("ACE_wrappers"):
    shutil.rmtree("ACE_wrappers")

shutil.unpack_archive("ACE-6.3.0.zip")
shutil.copy("./config.h", "./ACE_wrappers/ace")