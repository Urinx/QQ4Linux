from distutils.core import setup
import py2exe
import sys
 
#this allows to run it with a simple double click.
sys.argv.append('py2exe')
 
py2exe_options = {
        "includes": ["sip"],
        "dll_excludes": ["MSVCP90.dll",],
        "compressed": 1,
        "optimize": 2,
        "ascii": 0,
        "bundle_files": 1,
        }
 
setup(
      name = 'QQ4Linux',
      version = '1.5',
      windows = ['QQ4Linux.py',], 
      zipfile = None,
      options = {'py2exe': py2exe_options},
      data_files=[('img',
        ['img/LinuxQQ.png','img/apple.png','img/head.png','img/iphone-big-image.png'])],
      )