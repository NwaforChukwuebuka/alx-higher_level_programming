#include <Python.h>

/**
 * print_python_list_info - Prints basic info about Python lists.
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p)
{
	int sz, allocate, x;
	PyObject *object;

	sz = Py_SIZE(p);
	allocate = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", sz);
	printf("[*] Allocated = %d\n", allocate);

	for (x = 0; x < sz; x++)
	{
		printf("Element %d: ", x);

		object = PyList_GetItem(p, x);
		printf("%s\n", Py_TYPE(object)->tp_name);
	}
}
