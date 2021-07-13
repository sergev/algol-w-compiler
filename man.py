#!/usr/bin/python2
# man.py -- very simple markup preprocessor for man pages


import re, time, sys

def usage():
    print('''usage:  python2 man.py manpage.1.src manpage.1 MACRO="value"...

This is a rough preprocessor to convert marked  to man pages.
A summary of the markup commands you can use in your src file:

    ==heading==
    __itatics__
    **bold**
    {{MACRO}}

    {{{ 
    preformatted text blocks. 
    }}}
    ''')
    sys.exit(1)

if len(sys.argv) < 3: usage()

macros = {'DATE': time.strftime("%Y-%m-%d"),
          'YEAR': time.strftime("%Y")}
for arg in sys.argv[3:]:
    m = re.match(r'([A-Z][A-Za-z0-9_]+)=(.*)', arg)
    if m:
        macros[m.group(1)] = m.group(2)
    else: 
        usage()
        
repls = {
    r'\n*==(.+?)==\n+'   : r'\n.SH "\1"\n', # ==heading==
    r'__(.+?)__'     : r'\\fI\1\\fR',       # __itatics__
    r'\*\*(.+?)\*\*' : r'\\fB\1\\fR',       # **bold**
    r'\n+> *(.+?)\n' : r'\n.TP\n.B \1\n',   # >HEADING for definition lists
    r'\n{{{'         : r'\n.nf',            # {{{ preformatted text blocks. }}}
    r'\n}}}'         : r'\n.fi',
    r'{{(.+?)}}'     : lambda m: macros[m.group(1)],  # {{macro}} substitution
}

with file(sys.argv[1], "r") as f:
    page = f.read()

for pattern, repl in repls.items():
    page = re.sub(pattern, repl, page)

with file(sys.argv[2], "w") as f:
    f.write(page)
