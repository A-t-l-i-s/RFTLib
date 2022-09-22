#ifndef Key_SetSalt_HPP
#define Key_SetSalt_HPP





PyObject* Key_SetSalt(Rypto_Key_Type* self,PyObject* args,PyObject* kwargs){

	PyObject* salt;

	if (PyArg_ParseTuple(args,"O",&salt)){
		if (PyLong_Check(salt)){
			self->salt=salt;
		}
	}

	return Py_None;
}





#endif