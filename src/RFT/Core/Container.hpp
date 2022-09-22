#pragma once
#include"../require.hpp"
#include"Object.hpp"





class RFT_Container:public RFT_Object{
protected:
// ~~~~~~~~~~~ Variables ~~~~~~~~~~
	u_char* _buffer;
	u_int _size;
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



public:
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	// Constructor
	RFT_Container(){
	}

	RFT_Container(u_char* buffer,u_int size){
		this->_buffer=buffer;
		this->_size=size;
	}



	// Deconstructor
	~RFT_Container(){
	}
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



// ~~~~~~ General Functions ~~~~~
	// Data Pointer
	u_char* data(){
		return this->_buffer;
	}



	// Data Size
	u_int size(){
		return this->_size;
	}
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
};


