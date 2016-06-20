/* Indicate lack of support for ANSI C

Orgy Support:
	C99 and higher
	C++11 and higher
*/
#ifndef __cplusplus
#if __STDC_VERSION__ < 199901L
#error C version not supported. Please use a C99 compiler (pref. GCC)
#endif
#elif __cplusplus <= 199711L
#error C++ version not supported. Please use a C++11 compiler (pref. GCC)
#endif
