#ifndef Marshal_HPP
#define Marshal_HPP





PyObject* toBytes(PyObject* object){
	PyObject* newObject;

	newObject=PyObject_CallMethod(pickle,"dumps","O",object);
	newObject=PyObject_CallMethod(zlib,"compress","O",newObject);



	if (newObject==NULL){
		PyErr_Clear();
		newObject=Py_BuildValue("z",NULL);
	}
	

	return newObject;
}





PyObject* fromBytes(PyObject* object){
	PyObject* newObject;

	if (PyBytes_Check(object)){
		newObject=PyObject_CallMethod(zlib,"decompress","O",object);
		newObject=PyObject_CallMethod(pickle,"loads","O",newObject);
	} else {
		newObject=Py_BuildValue("z",NULL);
	}

	return newObject;
}





#endif