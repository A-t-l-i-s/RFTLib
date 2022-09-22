#ifndef Key_Init_HPP
#define Key_Init_HPP





int Rypto_Key_Init(Rypto_Key_Type* self,PyObject* args,PyObject* kwargs){


	self->random=PyObject_CallMethod(Module_Random,"Random",NULL);

	self->salt=Py_BuildValue("i",0);
	self->seed=Py_BuildValue("i",0);


	return 0;
}





#endif