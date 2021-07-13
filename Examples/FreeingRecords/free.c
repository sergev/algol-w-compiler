#include <awe.h>
#include <malloc.h>

  /* This frees a record in Windows systems, where records are allocated by malloc.

     A little run-time type checking is thrown in for free.

     Structures allocated by GC_ALLOC must not be deallocated with 'free'.
     The #ifdef directive makes the function harmless on Unix systems. */

void free_algol_record (void *r)
{
  if (r == NULL)
      _awe_error(_awe_HERE, "Attempted to free a reference to NULL.");

  if (r == _awe_uninitialized_reference)
      _awe_error(_awe_HERE, "Attempted to free an uninitialized reference variable.");

#ifdef __CYGWIN__
   free(r);
#endif
}
