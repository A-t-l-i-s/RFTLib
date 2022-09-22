#ifndef Methods_fromBytes_HPP
#define Methods_fromBytes_HPP





PyObject* DataServer_fromBytes(PyObject* self,PyObject* args){

	PyObject* data;
	PyObject* object;

	if (PyArg_ParseTuple(args,"O",&object)){
		data=fromBytes(object);
	}

	return Py_BuildValue("O",data);
}





#endif