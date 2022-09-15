#pragma once
#include"../require.hpp"
#include"Buffer.hpp"
#include"../Core/Object.hpp"
#include"../Core/Container.hpp"

typedef vector<u_char> RFT_Vector_Type;






class RFT_Vector:public RFT_Object{
protected:
// ~~~~~~~~~~~ Variables ~~~~~~~~~~
	RFT_Vector_Type _array;
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
			this->_array[index]=chr;
		} else if (index==this->size()){
			this->add(chr);
		}
	}



	// Get Char from Buffer
	u_char get(u_int index){
		if (this->belowRange(index)){
			return this->_array[index];
		} else {
			return 0;
		}
	}



	// Add Char to Buffer
	void add(u_char value){
		this->_array.push_back(value);
	}



	// Fill Buffer
	void fill(u_char value){
		memset(
			this->_array.data(),
			value,
			this->_array.size()
		);
	}



	// Resize Buffer
	void resize(u_int newSize){
		this->_array.resize(newSize);
	}



	// Clear Buffer
	void clear(){
		this->_array.clear();
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
		return this->_array.data();
	}



	// Get Size
	u_int size(){
		return this->_array.size();
	}
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



// ~~~~~~~~~~~ Operators ~~~~~~~~~~
	u_char operator[](u_int index){
		return this->get(index);
	}



	friend std::ostream& operator<<(std::ostream&,RFT_Vector);
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
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



// ~~~~~~~~~~~ Iterators ~~~~~~~~~~
	// Normal Iterator
	RFT_Vector_Type::iterator begin(){
		return this->_array.begin();
	}

	RFT_Vector_Type::iterator end(){
		return this->_array.end();
	}



	// Constant Iterator
	RFT_Vector_Type::const_iterator cbegin(){
		return this->_array.cbegin();
	}

	RFT_Vector_Type::const_iterator cend(){
		return this->_array.cend();
	}



	// Reversed Iterator
	RFT_Vector_Type::reverse_iterator rbegin(){
		return this->_array.rbegin();
	}

	RFT_Vector_Type::reverse_iterator rend(){
		return this->_array.rend();
	}



	// Constant Reversed Iterator
	RFT_Vector_Type::const_reverse_iterator crbegin(){
		return this->_array.crbegin();
	}

	RFT_Vector_Type::const_reverse_iterator crend(){
		return this->_array.crend();
	}
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



// ~~~~~~~~~~~~ Assign ~~~~~~~~~~~~
	void assign(u_int index,u_char* value,u_int size){
		for (u_int i=0;i<size;i++){
			if (this->belowRange(index)){
				this->_array[index]=value[i];
			} else {
				this->_array.push_back(value[i]);
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



// ~~~~~~~~~~~~ Insert ~~~~~~~~~~~~
	void insert(u_int index,u_char* value,u_int size){
		if (not this->inRange(index)){
			index=0;
		}

		this->_array.insert(
			this->_array.begin()+index,
			value,
			value+size
		);
	}


	void insert(u_int index,RFT_Object value){
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


	void append(RFT_Object value){
		this->append(
			value.data(),
			value.size()
		);
	}
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
};

