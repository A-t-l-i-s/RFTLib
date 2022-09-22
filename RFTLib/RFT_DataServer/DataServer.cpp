#ifndef DataServer_CPP
#define DataServer_CPP

#include<Require.hpp>





PyMODINIT_FUNC PyInit_DataServer(){
	PyObject* module=PyModule_Create(&DataServer_Module);



	zlib=PyImport_ImportModule("zlib");
	pickle=PyImport_ImportModule("_pickle");



	return module;
}





#endif





/*
@EXT C++

@BIT 64
@DLL true

@OUT DataServer.pyd
@EXR -s

@INC include
@INC /Python/include

@LBP /Python/libs

@LIB python3
@LIB python310

@END

@RUN python __main__.py
*/
