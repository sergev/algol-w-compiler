#!/usr/bin/python2
# man.py -- very simple markup preprocessor for man pages

import re, time, sys

def usage():
    print 'usage:  python man.py manpage.1.src manpage.1 VARIABLE="value"...'
    sys.exit(1)

if len(sys.argv) < 3: usage()

variables = {'DATE': time.strftime("%Y-%m-%d")}
for arg in sys.argv[3:]:
    match = re.match(r'([A-Z][A-Za-z0-9_]+)=(.*)', arg)
    if match:
        variables[match.group(1)] = match.group(2)
    else: 
        usage()
        
repls = {
    r'\n*==(.+?)==\n+'   : r'\n.SH "\1"\n', # ==heading==
    r'__(.+?)__'     : r'\\fI\1\\fR',       # __itatics__
    r'\*\*(.+?)\*\*' : r'\\fB\1\\fR',       # **bold**
    r'\n+> *(.+?)\n' : r'\n.TP\n.B \1\n',   # >HEADING for definition lists
    r'\n{{{'         : r'\n.nf',            # {{{ preformatted text blocks. }}}
    r'\n}}}'         : r'\n.fi',
    r'{{(.+?)}}'     : lambda m: variables[m.group(1)],  # {{variable}} substitution
}

with file(sys.argv[1], "r") as f:
    page = f.read()

for pattern, repl in repls.items():
    page = re.sub(pattern, repl, page)

with file(sys.argv[2], "w") as f:
    f.write(page)
