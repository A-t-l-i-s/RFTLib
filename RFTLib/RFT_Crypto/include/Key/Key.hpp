#ifndef Key_HPP
#define Key_HPP





typedef struct{
	PyObject_HEAD


	PyObject* random;

	PyObject* salt;
	PyObject* seed;


} Rypto_Key_Type;





#include<Key/New.hpp>
#include<Key/Init.hpp>
#include<Key/DeInit.hpp>

#include<Key/SetSalt.hpp>
#include<Key/SetSeed.hpp>





static PyMemberDef Rypto_Key_Members[]={
	{"random",T_OBJECT,offsetof(Rypto_Key_Type,random),READONLY,""},
	
	{"salt",T_OBJECT,offsetof(Rypto_Key_Type,salt),READONLY,""},
	{"seed",T_OBJECT,offsetof(Rypto_Key_Type,seed),READONLY,""},
{}};





static PyMethodDef Rypto_Key_Methods[]={
	{"setSalt",(PyCFunction)Key_SetSalt,METH_VARARGS,""},
	{"setSeed",(PyCFunction)Key_SetSeed,METH_VARARGS,""},
{}};





static PyTypeObject Rypto_Key={
	PyVarObject_HEAD_INIT(NULL,0)
	"Rypto.Key",
	sizeof(Rypto_Key_Type),
	0,
	(destructor)Rypto_Key_DeInit,
	0,
	0,
	0,
	0,
	0,
	0,
	0,
	0,
	0,
	0,
	0,
	0,
	0,
	0,
	Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE,
	"",
	0,
	0,
	0,
	0,
	0,
	0,
	Rypto_Key_Methods,
	Rypto_Key_Members,
	0,
	0,
	0,
	0,
	0,
	0,
	(initproc)Rypto_Key_Init,
	0,
	Rypto_Key_New,
};





#endif