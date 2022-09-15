#pragma once
#include"../require.hpp"
#include"../Core/Object.hpp"
#include"../Core/Container.hpp"







class RFT_Buffer:public RFT_Object{
public:
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	// Constructor
	RFT_Buffer(){
		this->_size=0;
	}

	RFT_Buffer(u_int size){
		this->_buffer=new u_char[size];

		this->_size=size;
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
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



// ~~~~~~~~~~~ Operators ~~~~~~~~~~
	u_char operator[](u_int index){
		return this->get(index);
	}



	friend std::ostream& operator<<(std::ostream&,RFT_Buffer);
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
		for (u_int i=0;i<size;i++){
			if (this->belowRange(index)){
				this->_buffer[index]=value[i];
			} else {
				break;
			}
			
			index++;
		}
	}


	void assign(u_int index,RFT_Object value){
		this->assign(
			index,
			value.data(),
			value.size()
		);
	}
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
};

