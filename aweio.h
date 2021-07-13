/* aweio.h -- this exposes the aweio module's Printer and Scanner types

If you understand these then you can write external procedures that redirect I/O to files.

--

This file is part of Awe. Copyright 2012 Glyn Webster.

This file is free software: you can redistribute it and/or modify it
under the terms of the GNU Limited General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Awe is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU Limited General Public
License along with Awe.  If not, see <http://www.gnu.org/licenses/>.

*/

#include <stdio.h>
#include <stdbool.h>


#define Scanner_BUFSIZE 512


typedef struct {
    FILE *input;
    char *input_name;
    bool eof;
    int state;
    int line;
    int column;
    int start_line;
    unsigned char buffer[Scanner_BUFSIZE];
    int buflen;
} _awe_Scanner;


typedef struct {
    FILE *output;
    int page;         /* The page in the printer, first page = 1 */
    int line;         /* The line the virtual printhead is in, first line = 1 */
    int column;       /* The column the virtual printhead should be in, first column = 1 */
    int true_column;  /* The column the printhead is really in, the printhead stops short when
                         printing string columns and the spaces after fields, those will not be
                         printed if they appear at the end of a line. */
} _awe_Printer;


extern _awe_Scanner _awe_stdin_scanner;   /* Input scanner reading from the standard input */
extern _awe_Scanner *_awe_active_scanner; /* The scanner in use. */

extern _awe_Printer _awe_stdout_printer;  /* Printer writing to the standard output */
extern _awe_Printer *_awe_active_printer; /* The printer in use. */


/* Note, 'input_name' should be NULL or point to a string that will remain
   allocated until the scanner is no longer in use. */

void _awe_Scanner_initialize (_awe_Scanner *scanner, FILE *file, char *input_name);


void _awe_Printer_initialize (_awe_Printer *printer, FILE *file);

void _awe_Printer_finalize (_awe_loc loc, _awe_Printer *printer);  /* Note: does not close the file. */


/* end */
