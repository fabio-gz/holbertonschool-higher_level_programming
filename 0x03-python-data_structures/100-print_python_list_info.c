#include <Python.h>
#include <stdio.h>
/**
 *print_python_list_info - print basic info about Python lists
 *@p: pointer to object
 */
void print_python_list_info(PyObject *p)
{
	unsigned int n;

	printf("[*] Size of the Python List = %lu\n", Py_SIZE(p));
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);

	for (n = 0; n < PyList_Size(p); n++)
	{
		printf("Element %d: %s\n", n, Py_TYPE(PyList_GetItem(p, n))->tp_name);
	}
}
