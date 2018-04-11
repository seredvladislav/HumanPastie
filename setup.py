import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["pyperclip"],
                     "zip_include_packages": "*",
                     "zip_exclude_packages": ""
                     # "excludes": ["tkinter"]
                     }

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
# if sys.platform == "win32":
#   base = "Win32GUI"

setup(name="HumanPastie",
      version="0.1",
      description="Human Pastie",
      options={"build_exe": build_exe_options, },
      executables=[Executable("HumanPastie.py", base=base)]

      )

#
