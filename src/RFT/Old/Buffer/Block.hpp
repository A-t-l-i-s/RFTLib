#pragma once
#include"../require.hpp"
#include"../Buffer/Buffer.hpp"





class RFT_Block{
protected:
// ~~~~~~~~~~~ Variables ~~~~~~~~~~
	u_char* _buffer;

	u_int _blockSize=512;
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



public:
// ~~~ Constructor/Deconstructor ~~
	// Constructor
	RFT_Block(u_int blockSize){
		this->_blockSize=blockSize;

		this->_buffer=new u_char[blockSize];
	}



	// Deconstructor
	~RFT_Block(){
		free(this->_buffer);
	}
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	u_char* data(){
		return this->_buffer;
	}
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
};


