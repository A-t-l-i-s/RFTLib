#ifndef Key_New_HPP
#define Key_New_HPP





PyObject* Rypto_Key_New(PyTypeObject* type,PyObject* args,PyObject* kwargs){
	Rypto_Key_Type* self=(Rypto_Key_Type*)type->tp_alloc(type,0);
    
    return (PyObject*)self;
}





#endif