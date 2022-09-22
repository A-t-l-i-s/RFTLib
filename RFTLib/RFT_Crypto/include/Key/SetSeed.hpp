#ifndef Key_SetSeed_HPP
#define Key_SetSeed_HPP





PyObject* Key_SetSeed(Rypto_Key_Type* self,PyObject* args,PyObject* kwargs){

	PyObject* seed;

	if (PyArg_ParseTuple(args,"O",&seed)){
		if (PyLong_Check(seed)){
			self->seed=seed;

			PyObject_CallMethod(self->random,"seed","O",seed);
		}
	}

	return Py_None;
}





#endif