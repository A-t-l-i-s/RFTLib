#pragma once
#include"../require.hpp"
#include"../Core/Object.hpp"







class RFT_Buffer:public RFT_Object{
protected:
// ~~~~~~~~~~~ Variables ~~~~~~~~~~
	u_int _size;
	u_char* _buffer;
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



public:
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	// Constructor
	RFT_Buffer(){
		this->_size=0;
		this->_buffer=(u_char*)malloc(0);
	}

	RFT_Buffer(u_int size){
		this->_size=size;
		this->_buffer=(u_char*)malloc(size);
	}



	// Deconstructor
	~RFT_Buffer(){
	}
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



// ~~~~~~ General Functions ~~~~~
	// Set Char of Buffer
	void set(u_int index,u_char chr){
		if (this->belowRange(index)){
			this->_buffer[index]=chr;
		}
	}



	// Get Char from Buffer
	u_char get(u_int index){
		if (this->belowRange(index)){
			return this->_buffer[index];
		} else {
			return 0;
		}
	}



	// Fill Buffer
	void fill(u_char value){
		memset(
			this->_buffer,
			value,
			this->_size
		);
	}



	// Reverse Buffer
	void reverse(){
		std::reverse(
			this->_buffer,
			this->_buffer+this->_size
		);
	}



	// Resize Pointer
	void resize(u_int size){
		this->_size=size;

		this->_buffer=(u_char*)realloc(
			this->_buffer,
			this->_size
		);
	}



	// Free Pointer
	void free(){
		if (this->_size){
			this->_size=0;

			std::free(this->_buffer);
		}
	}



	// Data Pointer
	u_char* data(){
		return this->_buffer;
	}



	// Data Size
	u_int size(){
		return this->_size;
	}
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



// ~~~~~~~~~~~ Operators ~~~~~~~~~~
	u_char operator[](u_int index){
		return this->get(index);
	}



	RFT_Buffer operator=(RFT_Buffer value){
		this->resize(value.size());

		memcpy(
			this->_buffer,
			value.data(),
			this->_size
		);

		value.free();

		return *this;
	}
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



// ~~~~~~~~~~~~~ Utils ~~~~~~~~~~~~
	// If given Index is in Buffer's Range
	bool inRange(u_int index){
		return (index>=0 and index<=this->_size);
	}



	// If given Index is directly one below Buffer's Range
	bool belowRange(u_int index){
		return (index>=0 and index<this->_size);
	}



	// Convert Buffer to Hex Buffer
	RFT_Buffer asHex(bool upper=false){
		u_int size=this->size();

		RFT_Buffer out(size*2);

		u_char c1,c2;
		for (u_int i=0;i<size;i++){
			c1=HEX_CHARS[(this->get(size-1-i) & 0xF0) >> 4];
			c2=HEX_CHARS[(this->get(size-1-i) & 0x0F) >> 0];

			if (upper){
				c1=std::toupper(c1);
				c2=std::toupper(c2);
			}

			out.set(i*2,c1);
			out.set(i*2+1,c2);
		}

		return out;
	}



	// Get Buffer as String
	string asString(){
		return string(
			this->_buffer,
			this->_buffer+this->_size
		);
	}
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



// ~~~~~~~~~~~ Iterators ~~~~~~~~~~
	// Normal Iterator
	u_char* begin(){
		return this->_buffer;
	}

	u_char* end(){
		return this->_buffer+this->_size;
	}



	// Constant Iterator
	const u_char* cbegin(){
		return this->_buffer;
	}

	const u_char* cend(){
		return this->_buffer+this->_size;
	}
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



// ~~~~~~~~~~~~ Assign ~~~~~~~~~~~~
	void assign(u_int index,u_char* value,u_int size){
		memcpy(
			this->_buffer+index,
			value,
			size
		);
	}

	void assign(u_int index,RFT_Buffer value){
		this->assign(
			index,
			value.data(),
			value.size()
		);
	}
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
};

