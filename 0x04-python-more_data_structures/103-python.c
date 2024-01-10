#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *element;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", PyList_Size(p));
	printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < PyList_Size(p); i++)
	{
		element = PyList_GetItem(p, i);
		printf("Element %zd: %s\n", i, Py_TYPE(element)->tp_name);
		if (PyBytes_Check(element))
		{
			printf("[.] bytes object info\n");
			printf("  size: %zd\n", PyBytes_Size(element));
			printf("  trying string: %s\n", PyBytes_AsString(element));
			printf("  first 10 bytes: ");
			fflush(stdout);
			for (Py_ssize_t j = 0; j < 10 && j < PyBytes_Size(element); j++)
			{
				printf("%02x ", (unsigned char)PyBytes_AsString(element)[j]);
			}
			printf("\n");
		}
	}
}

void print_python_bytes(PyObject *p)
{
	printf("[.] bytes object info\n");
	printf("  size: %zd\n", PyBytes_Size(p));
	printf("  trying string: %s\n", PyBytes_AsString(p));
	printf("  first 10 bytes: ");
	fflush(stdout);
	for (Py_ssize_t i = 0; i < 10 && i < PyBytes_Size(p); i++)
	{
		printf("%02x ", (unsigned char)PyBytes_AsString(p)[i]);
	}
	printf("\n");
}
