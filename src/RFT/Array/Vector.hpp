#pragma once
#include"../require.hpp"
#include"Buffer.hpp"
#include"../Core/Object.hpp"
#include"../Core/Container.hpp"

typedef vector<u_char> RFT_Vector_Type;






class RFT_Vector:public RFT_Object{
protected:
// ~~~~~~~~~~~ Variables ~~~~~~~~~~
	RFT_Vector_Type _buffer;
	u_int _size;
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



public:
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	// Constructor
	RFT_Vector(){
	}



	// Deconstructor
	~RFT_Vector(){
	}
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



// ~~~~~~ General Functions ~~~~~
	// Set Char of Buffer
	void set(u_int index,u_char chr){
		if (this->belowRange(index)){
			this->_buffer[index]=chr;
		} else if (index==this->size()){
			this->add(chr);
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



	// Add Char to Buffer
	void add(u_char value){
		this->_buffer.push_back(value);
	}



	// Fill Buffer
	void fill(u_char value){
		memset(
			this->_buffer.data(),
			value,
			this->_buffer.size()
		);
	}



	// Resize Buffer
	void resize(u_int newSize){
		this->_buffer.resize(newSize);
	}



	// Clear Buffer
	void clear(){
		this->_buffer.clear();
	}



	// Reverse Buffer
	void reverse(){
		std::reverse(
			this->begin(),
			this->end()
		);
	}



	// Get Char Pointer
	u_char* data(){
		return this->_buffer.data();
	}



	// Get Size
	u_int size(){
		return this->_buffer.size();
	}
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



// ~~~~~~~~~~~ Operators ~~~~~~~~~~
	u_char operator[](u_int index){
		return this->get(index);
	}
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



// ~~~~~~~~~~~~~ Utils ~~~~~~~~~~~~
	// If given Index is in Buffer's Range
	bool inRange(u_int index){
		return (index>=0 and index<=this->size());
	}



	// If given Index is directly one below Buffer's Range
	bool belowRange(u_int index){
		return (index>=0 and index<this->size());
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
			this->begin(),
			this->end()
		);
	}
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



// ~~~~~~~~~~~ Iterators ~~~~~~~~~~
	// Normal Iterator
	RFT_Vector_Type::iterator begin(){
		return this->_buffer.begin();
	}

	RFT_Vector_Type::iterator end(){
		return this->_buffer.end();
	}



	// Constant Iterator
	RFT_Vector_Type::const_iterator cbegin(){
		return this->_buffer.cbegin();
	}

	RFT_Vector_Type::const_iterator cend(){
		return this->_buffer.cend();
	}



	// Reversed Iterator
	RFT_Vector_Type::reverse_iterator rbegin(){
		return this->_buffer.rbegin();
	}

	RFT_Vector_Type::reverse_iterator rend(){
		return this->_buffer.rend();
	}



	// Constant Reversed Iterator
	RFT_Vector_Type::const_reverse_iterator crbegin(){
		return this->_buffer.crbegin();
	}

	RFT_Vector_Type::const_reverse_iterator crend(){
		return this->_buffer.crend();
	}
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



// ~~~~~~~~~~~~ Assign ~~~~~~~~~~~~
	void assign(u_int index,u_char* value,u_int size){
		for (u_int i=0;i<size;i++){
			if (this->belowRange(index)){
				this->_buffer[index]=value[i];
			} else {
				this->_buffer.push_back(value[i]);
			}
			
			index++;
		}
	}


	void assign(u_int index,RFT_Buffer value){
		this->assign(
			index,
			value.data(),
			value.size()
		);
	}


	void assign(u_int index,RFT_Vector value){
		this->assign(
			index,
			value.data(),
			value.size()
		);
	}
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



// ~~~~~~~~~~~~ Insert ~~~~~~~~~~~~
	void insert(u_int index,u_char* value,u_int size){
		if (not this->inRange(index)){
			index=0;
		}

		this->_buffer.insert(
			this->_buffer.begin()+index,
			value,
			value+size
		);
	}


	void insert(u_int index,RFT_Buffer value){
		this->insert(
			index,
			value.data(),
			value.size()
		);
	}


	void insert(u_int index,RFT_Vector value){
		this->insert(
			index,
			value.data(),
			value.size()
		);
	}
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



// ~~~~~~~~~~~~ Append ~~~~~~~~~~~~
	void append(u_char* value,u_int size){
		this->insert(
			this->size(),
			value,
			size
		);
	}


	void append(RFT_Buffer value){
		this->append(
			value.data(),
			value.size()
		);
	}


	void append(RFT_Vector value){
		this->append(
			value.data(),
			value.size()
		);
	}
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
};

