#ifndef Methods_toBytes_HPP
#define Methods_toBytes_HPP





PyObject* DataServer_toBytes(PyObject* self,PyObject* args){

	PyObject* data;
	PyObject* object;

	if (PyArg_ParseTuple(args,"O",&object)){
		data=toBytes(object);
	}

	return Py_BuildValue("O",data);
}





#endif