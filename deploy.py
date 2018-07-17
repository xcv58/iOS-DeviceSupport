#!/usr/bin/env python
from os import listdir, path
import zipfile

XCODE = '/Applications/Xcode.app'
TARGET= '{}/Contents/Developer/Platforms/iPhoneOS.platform/DeviceSupport/'.format(XCODE)
SRC = path.join(path.dirname(path.abspath(__file__)), 'DeviceSupport')

def unzip_file(name):
  f = path.join(SRC, name + '.zip')
  print 'Unzip file', f, 'to', TARGET
  zip_ref = zipfile.ZipFile(f, 'r')
  zip_ref.extractall(TARGET)
  zip_ref.close()


exist = listdir(TARGET)
all_files = [i.replace('.zip', '') for i in listdir(SRC) if i.endswith('.zip')]
new_files = list(set(all_files) - set(exist))
for i in new_files:
  unzip_file(i)
