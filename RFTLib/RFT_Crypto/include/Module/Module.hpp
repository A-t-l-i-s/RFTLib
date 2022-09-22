#ifndef Module_HPP
#define Module_HPP





static PyMethodDef Rypto_Methods[]={
	// {"Init",(PyCFunction)Rypto_Module_Init,METH_NOARGS,""},
{NULL}};



static PyModuleDef Rypto_Module={PyModuleDef_HEAD_INIT,"Rypto",NULL,-1,Rypto_Methods};





#endif