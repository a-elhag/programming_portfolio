#include <stdio.h>
#include <limits.h>

main()
{
	printf("Range of unsigned char is [%d, %d].\n", CHAR_MIN, CHAR_MAX);
	printf("Range of signed char is [%d, %d].\n", SCHAR_MIN, SCHAR_MAX);
	printf("Range of an short is [%d, %d].\n", SHRT_MIN, SHRT_MAX);
	printf("Range of an int is [%d, %d].\n", INT_MIN, INT_MAX);
	printf("Range of a long is [%ld, %ld].\n", LONG_MIN, LONG_MAX);
	printf("Bits in a char [%d]\n", CHAR_BIT);

	return 0;
}
