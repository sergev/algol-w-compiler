template = '''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">
  <head>
    <meta http-equiv="content-type" content="text/html; charset=utf-8"/>
    <title>%s</title>
  </head>
<body>
<pre>%s</pre>
</body>
</html>
'''

import sys, cgi

def x(s): return cgi.escape(s, quote=True)

sys.stdout.write(template % (x(sys.argv[1]), x(sys.stdin.read())))
