#include <Python.h>
#include <stdbool.h>
#include <stdlib.h>
#include <math.h>

/**
 * Generate prime numbers up to n using Sieve of Eratosthenes.
 *
 * @param n The upper bound (exclusive)
 * @return A Python list of prime numbers
 */
static PyObject *primes_c(PyObject *self, PyObject *args)
{
    long n;

    if (!PyArg_ParseTuple(args, "l", &n))
    {
        return NULL;
    }

    if (n < 2)
    {
        return PyList_New(0);
    }

    bool *sieve = (bool *)calloc(n, sizeof(bool));
    if (!sieve)
    {
        PyErr_NoMemory();
        return NULL;
    }

    for (long i = 0; i < n; i++)
    {
        sieve[i] = true;
    }

    long sqrt_n = (long)sqrt((double)n);
    for (long i = 2; i <= sqrt_n; i++)
    {
        if (sieve[i])
        {
            for (long j = i * i; j < n; j += i)
            {
                sieve[j] = false;
            }
        }
    }

    long count = 0;
    for (long i = 2; i < n; i++)
    {
        if (sieve[i])
            count++;
    }

    PyObject *list = PyList_New(count);
    if (!list)
    {
        free(sieve);
        return NULL;
    }

    long idx = 0;
    for (long i = 2; i < n; i++)
    {
        if (sieve[i])
        {
            PyObject *pyNum = PyLong_FromLong(i);
            if (!pyNum)
            {
                Py_DECREF(list);
                free(sieve);
                return NULL;
            }

            PyList_SET_ITEM(list, idx++, pyNum);
        }
    }

    free(sieve);
    return list;
}

static PyMethodDef PrimeMethods[] = {
    {"primes_c", primes_c, METH_VARARGS,
     "Generate prime numbers up to n using Sieve of Eratosthenes"},
    {NULL, NULL, 0, NULL} // Sentinel
};

static struct PyModuleDef primemodule = {
    PyModuleDef_HEAD_INIT,
    "prime_c",
    "Prime number generation in C",
    -1,
    PrimeMethods};

PyMODINIT_FUNC PyInit_prime_c(void)
{
    return PyModule_Create(&primemodule);
}
