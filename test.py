import openpyxl as xl
import os
from os import chdir
from os.path import dirname
from sys import executable

path = os.getcwd()
# path = chdir(dirname(executable))
# print(chdir(dirname(executable)))
wb = xl.Workbook()
wb.save(path + '/' + 'test.xlsx')
# print('path')