#pragma once
#include"../require.hpp"
#include"Object.hpp"





class RFT_Container:public RFT_Object{
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
};


