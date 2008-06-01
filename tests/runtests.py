#!/usr/bin/env python

''' Stolen and adapted from pygobject '''

import glob
import os
import sys
import unittest
import webbrowser
import HTMLTestRunner

fp = file('test_report.html', 'wb')

program = None
if len(sys.argv) == 3:
    buildDir = sys.argv[1]
    srcDir = sys.argv[2]
else:
    if len(sys.argv) == 2:
        program = sys.argv[1]
        if program.endswith('.py'):
            program = program[:-3]
    buildDir = '..'
    srcDir = '.'

SKIP_FILES = ['runtests']

dir = os.path.split(os.path.abspath(__file__))[0]
os.chdir(dir)

def gettestnames():
    files = glob.glob('*.py')
    names = map(lambda x: x[:-3], files)
    map(names.remove, SKIP_FILES)
    return names

suite = unittest.TestSuite()
loader = unittest.TestLoader()

for name in gettestnames():
    if program and program not in name:
        continue
    suite.addTest(loader.loadTestsFromName(name))

runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                       title='PyGooCanvas bindings tests',
                                       description='Testing.....')
runner.run(suite)
fp.close()

webbrowser.open('test_report.html')