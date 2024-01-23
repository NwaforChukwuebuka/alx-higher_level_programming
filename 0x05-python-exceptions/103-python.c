#include </usr/include/python3.8/Python.h>

/**
 * print_python_list - Prints basic info about Python lists.
 * @p: Pointer to PyObject list object.
 */
void print_python_list(PyObject *p)
{
    Py_ssize_t sz, i;
    const char *type;
    PyListObject *list = (PyListObject *)p;
    PyVarObject *var = (PyVarObject *)p;

    sz = var->ob_size;
    i = 0;

    fflush(stdout);

    printf("[*] Python list info\n");
    if (strcmp(p->ob_type->tp_name, "list") != 0)
    {
        printf("  [ERROR] Invalid List Object\n");
        return;
    }

    printf("[*] Size of the Python List = %ld\n", sz);
    printf("[*] Allocated = %ld\n", list->allocated);

    while (i < sz)
    {
        type = list->ob_item[i]->ob_type->tp_name;
        printf("Element %ld: %s\n", i, type);
        i++;
    }
}

/**
 * print_python_bytes - Prints basic info about Python byte objects.
 * @p: Pointer to PyObject byte object.
 */
void print_python_bytes(PyObject *p)
{
    Py_ssize_t sz, i;
    PyBytesObject *bytes = (PyBytesObject *)p;

    i = 0;

    fflush(stdout);

    printf("[.] bytes object info\n");
    if (strcmp(p->ob_type->tp_name, "bytes") != 0)
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    sz = ((PyVarObject *)p)->ob_size;
    printf("  size: %ld\n", sz);
    printf("  trying string: %s\n", bytes->ob_sval);

    if (sz >= 10)
        sz = 10;

    printf("  first %ld bytes: ", sz);
    for (; i < sz; i++)
    {
        printf("%02hhx", bytes->ob_sval[i]);
        if (i == (sz - 1))
            printf("\n");
        else
            printf(" ");
    }
}

/**
 * print_python_float - Prints basic info about Python float objects.
 * @p: Pointer to PyObject float object.
 */
void print_python_float(PyObject *p)
{
    char *buf = NULL;

    PyFloatObject *float_obj = (PyFloatObject *)p;

    fflush(stdout);

    printf("[.] float object info\n");
    if (strcmp(p->ob_type->tp_name, "float") != 0)
    {
        printf("  [ERROR] Invalid Float Object\n");
        return;
    }

    buf = PyOS_double_to_string(float_obj->ob_fval, 'r', 0,
                                Py_DTSF_ADD_DOT_0, NULL);
    printf("  value: %s\n", buf);
    PyMem_Free(buf);
}
