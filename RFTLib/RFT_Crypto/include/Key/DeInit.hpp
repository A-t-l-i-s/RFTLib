#ifndef Key_DeInit_HPP
#define Key_DeInit_HPP





void Rypto_Key_DeInit(Rypto_Key_Type* self){
    Py_TYPE(self)->tp_free((PyObject*)self);
}





#endif