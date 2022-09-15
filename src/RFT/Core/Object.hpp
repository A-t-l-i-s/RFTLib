#pragma once
#include"../require.hpp"





class RFT_Object{
protected:
// ~~~~~~~~~~~ Variables ~~~~~~~~~~
	u_char* _buffer;
	u_int _size;
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



public:
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	// Constructor
	RFT_Object(){
		this->_size=0;
	}



	// Deconstructor
	~RFT_Object(){
	}
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



// ~~~~~~~~~~~ Operators ~~~~~~~~~~
	friend std::ostream& operator<<(std::ostream&,RFT_Object);
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



// ~~~~~~~~~~~ Functions ~~~~~~~~~~
	// Get Buffer Pointer
	u_char* data(){
		return this->_buffer;
	}


	// Get Buffer Size
	u_int size(){
		return this->_size;
	}
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
};


