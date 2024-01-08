#include <stdio.h>
#include <stdlib.h>
#include <Python.h>
/**
 * print_python_list_info - function that prints some basic
 *info about Python lists
 * @p: python list
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	int element;

	printf("[*] Size of the Python List = %lu\n", Py_SIZE(p));
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
	element = 0;
	while (element < Py_SIZE(p))
	{
		printf("Element %d: %s\n", elem, Py_TYPE(PyList_GetItem(p, elem))->tp_name);
		element++;
	}
}
