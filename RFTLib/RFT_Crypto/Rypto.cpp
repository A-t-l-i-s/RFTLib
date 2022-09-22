#ifndef Rypto_CPP
#define Rypto_CPP

#include<Require.hpp>





PyMODINIT_FUNC PyInit_Rypto(){
	PyObject* module=PyModule_Create(&Rypto_Module);



	// setup curl
	Curl_Headers=curl_slist_append(Curl_Headers,"Accept: application/json");
	Curl_Headers=curl_slist_append(Curl_Headers,"User-Agent: GeoEncryption/1.0");
	Curl_Headers=curl_slist_append(Curl_Headers,"Authorization: Bearer 5aa42fc4afd30e");


	curl_easy_setopt(Curl,CURLOPT_VERBOSE,false);
	curl_easy_setopt(Curl,CURLOPT_SSL_VERIFYPEER,false);
	curl_easy_setopt(Curl,CURLOPT_HTTPHEADER,Curl_Headers);
	curl_easy_setopt(Curl,CURLOPT_WRITEFUNCTION,Curl_Callback);



	// import modules
	Module_Random=PyImport_ImportModule("random");
	Module_Hashlib=PyImport_ImportModule("hashlib");



	// init Key type
	PyType_Ready(&Rypto_Key);
	Py_INCREF(&Rypto_Key);

	PyModule_AddObject(module,"Key",(PyObject*)&Rypto_Key);



	return module;
}





#endif





/*
@EXT C++

@BIT 64
@DLL true
@WIN false
@VER c++20

@EXR -s

@INC include
@INC /Python/include

@LBP /Python/libs

@LIB curl
@LIB python3
@LIB python310

@OUT Rypto.pyd

@END


@RUN python __main__.py
*/