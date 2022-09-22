#ifndef Require_HPP
#define Require_HPP

#define PY_SSIZE_T_CLEAN



#include<Python.h>



PyObject* zlib;
PyObject* pickle;



#include<Marshal.hpp>
#include<Methods.hpp>



static PyMethodDef DataServer_Methods[]={
	{"toBytes",DataServer_toBytes,METH_VARARGS,""},
	{"fromBytes",DataServer_fromBytes,METH_VARARGS,""},
{NULL,NULL,0,NULL}};


static PyModuleDef DataServer_Module={PyModuleDef_HEAD_INIT,"DataServer",NULL,-1,DataServer_Methods};








#endif