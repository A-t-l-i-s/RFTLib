#pragma once
#include"../require.hpp"
#include"../Structs/Structs.hpp"







// ~~~~~~~~~~~~ Macros ~~~~~~~~~~~~
	#define RFT_BUFFER_INSERT_CHAR_P					\
		u_char chr;										\
														\
		for (u_int i=0;i<size;i++){ 		 			\
			if (swap.value){							\
				chr=value[(size-1)-i];					\
			} else {									\
				chr=value[i];							\
			}											\
														\
			this->_buffer.insert( 		 				\
				this->_buffer.begin()+index+i, 			\
				chr 		 		 	 				\
			);		 		 		 		 			\
		}												\



	#define RFT_BUFFER_INSERT_BASIC						\
		u_char* buf=(u_char*)&value;					\
		u_int size=sizeof(value);						\
														\
		u_char chr;										\
														\
		for (u_int i=0;i<size;i++){ 		 			\
			if (swap.value){							\
				chr=buf[(size-1)-i];					\
			} else {									\
				chr=buf[i];								\
			}											\
														\
			this->_buffer.insert( 		 				\
				this->_buffer.begin()+index+i, 		 	\
				chr 		 		 	 				\
			);		 		 		 		 			\
		}												\



	#define RFT_BUFFER_INSERT_ITERATOR					\
		if (swap.value){								\
			this->_buffer.insert( 		 		 		\
				this->_buffer.begin()+index, 			\
				value.rbegin(), 		 		 		\
				value.rend() 		 		 	 		\
			);		 		 		 		 			\
		} else {										\
			this->_buffer.insert( 		 		 		\
				this->_buffer.begin()+index, 			\
				value.begin(), 		 		 	 		\
				value.end() 		 		 	 		\
			);		 		 		 		 			\
		}												\
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~







class RFT_Buffer{
protected:
// ~~~~~~~~~~~ Variables ~~~~~~~~~~
	RFT_BUFFER_TYPE _buffer;
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



public:
// ~~~ Constructor/Deconstructor ~~
	// Constructor
	RFT_Buffer(){
	}



	// Deconstructor
	~RFT_Buffer(){
	}
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



// ~~~~~~~~ Data Management ~~~~~~~
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



	friend std::ostream& operator<<(std::ostream&,RFT_Buffer);
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



// ~~~~~~~~~~~~~ Utils ~~~~~~~~~~~~
	// If given Index is in Buffer's Range
	bool inRange(u_int index){
		if (index>=0 and index<=this->size())
			return true;
		else
			return false;
	}



	// If given Index is directly one below Buffer's Range
	bool belowRange(u_int index){
		if (index>=0 and index<this->size())
			return true;
		else
			return false;
	}
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



// ~~~~~~~~~~ Converters ~~~~~~~~~~
	// Convert Buffer to Hex Buffer
	RFT_Buffer asHex(bool upper=false){
		RFT_Buffer out;

		u_int size=this->size();

		u_char c1,c2;
		for (u_int i=0;i<size;i++){
			c1=HEX_CHARS[(this->get(size-1-i) & 0xF0) >> 4];
			c2=HEX_CHARS[(this->get(size-1-i) & 0x0F) >> 0];

			if (upper){
				c1=std::toupper(c1);
				c2=std::toupper(c2);
			}

			out.add(c1);
			out.add(c2);
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
	RFT_BUFFER_TYPE::iterator begin(){
		return this->_buffer.begin();
	}

	RFT_BUFFER_TYPE::iterator end(){
		return this->_buffer.end();
	}



	// Constant Iterator
	RFT_BUFFER_TYPE::const_iterator cbegin(){
		return this->_buffer.cbegin();
	}

	RFT_BUFFER_TYPE::const_iterator cend(){
		return this->_buffer.cend();
	}



	// Reversed Iterator
	RFT_BUFFER_TYPE::reverse_iterator rbegin(){
		return this->_buffer.rbegin();
	}

	RFT_BUFFER_TYPE::reverse_iterator rend(){
		return this->_buffer.rend();
	}



	// Constant Reversed Iterator
	RFT_BUFFER_TYPE::const_reverse_iterator crbegin(){
		return this->_buffer.crbegin();
	}

	RFT_BUFFER_TYPE::const_reverse_iterator crend(){
		return this->_buffer.crend();
	}
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



// ~~~~~~~~~~~ Set Value ~~~~~~~~~~
	void setValue(u_char* value,u_int size,RFT_Structs::Swap swap=RFT_Structs::NoSwap){
		this->clear();

		u_int index=0;
		RFT_BUFFER_INSERT_CHAR_P
	}

	void setValue(char* value,u_int size,RFT_Structs::Swap swap=RFT_Structs::NoSwap){
		this->clear();

		u_int index=0;
		RFT_BUFFER_INSERT_CHAR_P
	}

	void setValue(const char* value,u_int size,RFT_Structs::Swap swap=RFT_Structs::NoSwap){
		this->clear();

		u_int index=0;
		RFT_BUFFER_INSERT_CHAR_P
	}


	void setValue(u_char* value,RFT_Structs::Swap swap=RFT_Structs::NoSwap){
		this->clear();

		u_int index=0;
		u_int size=strlen((char*)value);

		RFT_BUFFER_INSERT_CHAR_P
	}

	void setValue(char* value,RFT_Structs::Swap swap=RFT_Structs::NoSwap){
		this->clear();

		u_int index=0;
		u_int size=strlen(value);

		RFT_BUFFER_INSERT_CHAR_P
	}

	void setValue(const char* value,RFT_Structs::Swap swap=RFT_Structs::NoSwap){
		this->clear();

		u_int index=0;
		u_int size=strlen(value);

		RFT_BUFFER_INSERT_CHAR_P
	}



	void setValue(string value,RFT_Structs::Swap swap=RFT_Structs::NoSwap){
		this->clear();

		u_int index=0;
		RFT_BUFFER_INSERT_ITERATOR
	}



	void setValue(RFT_Buffer value,RFT_Structs::Swap swap=RFT_Structs::NoSwap){
		this->clear();

		u_int index=0;
		RFT_BUFFER_INSERT_ITERATOR
	}



	void setValue(uint8_t value,RFT_Structs::Swap swap=RFT_Structs::NoSwap){
		this->clear();

		u_int index=0;
		RFT_BUFFER_INSERT_BASIC
	}

	void setValue(int8_t value,RFT_Structs::Swap swap=RFT_Structs::NoSwap){
		this->clear();

		u_int index=0;
		RFT_BUFFER_INSERT_BASIC
	}


	void setValue(uint16_t value,RFT_Structs::Swap swap=RFT_Structs::NoSwap){
		this->clear();

		u_int index=0;
		RFT_BUFFER_INSERT_BASIC
	}

	void setValue(int16_t value,RFT_Structs::Swap swap=RFT_Structs::NoSwap){
		this->clear();

		u_int index=0;
		RFT_BUFFER_INSERT_BASIC
	}


	void setValue(uint32_t value,RFT_Structs::Swap swap=RFT_Structs::NoSwap){
		this->clear();

		u_int index=0;
		RFT_BUFFER_INSERT_BASIC
	}

	void setValue(int32_t value,RFT_Structs::Swap swap=RFT_Structs::NoSwap){
		this->clear();

		u_int index=0;
		RFT_BUFFER_INSERT_BASIC
	}


	void setValue(uint64_t value,RFT_Structs::Swap swap=RFT_Structs::NoSwap){
		this->clear();

		u_int index=0;
		RFT_BUFFER_INSERT_BASIC
	}

	void setValue(int64_t value,RFT_Structs::Swap swap=RFT_Structs::NoSwap){
		this->clear();

		u_int index=0;
		RFT_BUFFER_INSERT_BASIC
	}


	void setValue(float value,RFT_Structs::Swap swap=RFT_Structs::NoSwap){
		this->clear();

		u_int index=0;
		RFT_BUFFER_INSERT_BASIC
	}


	void setValue(double value,RFT_Structs::Swap swap=RFT_Structs::NoSwap){
		this->clear();

		u_int index=0;
		RFT_BUFFER_INSERT_BASIC
	}


	void setValue(long double value,RFT_Structs::Swap swap=RFT_Structs::NoSwap){
		this->clear();

		u_int index=0;
		RFT_BUFFER_INSERT_BASIC
	}
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



// ~~~~~~~~~~~~ Insert ~~~~~~~~~~~~
	void insert(u_int index,u_char* value,u_int size,RFT_Structs::Swap swap=RFT_Structs::NoSwap){
		RFT_BUFFER_INSERT_CHAR_P
	}

	void insert(u_int index,char* value,u_int size,RFT_Structs::Swap swap=RFT_Structs::NoSwap){
		RFT_BUFFER_INSERT_CHAR_P
	}

	void insert(u_int index,const char* value,u_int size,RFT_Structs::Swap swap=RFT_Structs::NoSwap){
		RFT_BUFFER_INSERT_CHAR_P
	}


	void insert(u_int index,u_char* value,RFT_Structs::Swap swap=RFT_Structs::NoSwap){
		u_int size=strlen((char*)value);

		RFT_BUFFER_INSERT_CHAR_P
	}

	void insert(u_int index,char* value,RFT_Structs::Swap swap=RFT_Structs::NoSwap){
		u_int size=strlen(value);

		RFT_BUFFER_INSERT_CHAR_P
	}

	void insert(u_int index,const char* value,RFT_Structs::Swap swap=RFT_Structs::NoSwap){
		u_int size=strlen(value);

		RFT_BUFFER_INSERT_CHAR_P
	}



	void insert(u_int index,string value,RFT_Structs::Swap swap=RFT_Structs::NoSwap){
		RFT_BUFFER_INSERT_ITERATOR
	}



	void insert(u_int index,RFT_Buffer value,RFT_Structs::Swap swap=RFT_Structs::NoSwap){
		RFT_BUFFER_INSERT_ITERATOR
	}



	void insert(u_int index,uint8_t value,RFT_Structs::Swap swap=RFT_Structs::NoSwap){
		RFT_BUFFER_INSERT_BASIC
	}

	void insert(u_int index,int8_t value,RFT_Structs::Swap swap=RFT_Structs::NoSwap){
		RFT_BUFFER_INSERT_BASIC
	}


	void insert(u_int index,uint16_t value,RFT_Structs::Swap swap=RFT_Structs::NoSwap){
		RFT_BUFFER_INSERT_BASIC
	}

	void insert(u_int index,int16_t value,RFT_Structs::Swap swap=RFT_Structs::NoSwap){
		RFT_BUFFER_INSERT_BASIC
	}


	void insert(u_int index,uint32_t value,RFT_Structs::Swap swap=RFT_Structs::NoSwap){
		RFT_BUFFER_INSERT_BASIC
	}

	void insert(u_int index,int32_t value,RFT_Structs::Swap swap=RFT_Structs::NoSwap){
		RFT_BUFFER_INSERT_BASIC
	}


	void insert(u_int index,uint64_t value,RFT_Structs::Swap swap=RFT_Structs::NoSwap){
		RFT_BUFFER_INSERT_BASIC
	}

	void insert(u_int index,int64_t value,RFT_Structs::Swap swap=RFT_Structs::NoSwap){
		RFT_BUFFER_INSERT_BASIC
	}


	void insert(u_int index,float value,RFT_Structs::Swap swap=RFT_Structs::NoSwap){
		RFT_BUFFER_INSERT_BASIC
	}


	void insert(u_int index,double value,RFT_Structs::Swap swap=RFT_Structs::NoSwap){
		RFT_BUFFER_INSERT_BASIC
	}


	void insert(u_int index,long double value,RFT_Structs::Swap swap=RFT_Structs::NoSwap){
		RFT_BUFFER_INSERT_BASIC
	}
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


// ~~~~~~~~~~~~ Append ~~~~~~~~~~~~
	void append(u_char* value,u_int size,RFT_Structs::Swap swap=RFT_Structs::NoSwap){
		u_int index=this->size();

		RFT_BUFFER_INSERT_CHAR_P
	}

	void append(char* value,u_int size,RFT_Structs::Swap swap=RFT_Structs::NoSwap){
		u_int index=this->size();
		
		RFT_BUFFER_INSERT_CHAR_P
	}

	void append(const char* value,u_int size,RFT_Structs::Swap swap=RFT_Structs::NoSwap){
		u_int index=this->size();
		
		RFT_BUFFER_INSERT_CHAR_P
	}


	void append(u_char* value,RFT_Structs::Swap swap=RFT_Structs::NoSwap){
		u_int index=this->size();
		
		u_int size=strlen((char*)value);

		RFT_BUFFER_INSERT_CHAR_P
	}

	void append(char* value,RFT_Structs::Swap swap=RFT_Structs::NoSwap){
		u_int index=this->size();
		
		u_int size=strlen(value);

		RFT_BUFFER_INSERT_CHAR_P
	}

	void append(const char* value,RFT_Structs::Swap swap=RFT_Structs::NoSwap){
		u_int index=this->size();
		
		u_int size=strlen(value);

		RFT_BUFFER_INSERT_CHAR_P
	}



	void append(string value,RFT_Structs::Swap swap=RFT_Structs::NoSwap){
		u_int index=this->size();
		
		RFT_BUFFER_INSERT_ITERATOR
	}



	void append(RFT_Buffer value,RFT_Structs::Swap swap=RFT_Structs::NoSwap){
		u_int index=this->size();
		
		RFT_BUFFER_INSERT_ITERATOR
	}



	void append(uint8_t value,RFT_Structs::Swap swap=RFT_Structs::NoSwap){
		u_int index=this->size();
		
		RFT_BUFFER_INSERT_BASIC
	}

	void append(int8_t value,RFT_Structs::Swap swap=RFT_Structs::NoSwap){
		u_int index=this->size();
		
		RFT_BUFFER_INSERT_BASIC
	}


	void append(uint16_t value,RFT_Structs::Swap swap=RFT_Structs::NoSwap){
		u_int index=this->size();
		
		RFT_BUFFER_INSERT_BASIC
	}

	void append(int16_t value,RFT_Structs::Swap swap=RFT_Structs::NoSwap){
		u_int index=this->size();
		
		RFT_BUFFER_INSERT_BASIC
	}


	void append(uint32_t value,RFT_Structs::Swap swap=RFT_Structs::NoSwap){
		u_int index=this->size();
		
		RFT_BUFFER_INSERT_BASIC
	}

	void append(int32_t value,RFT_Structs::Swap swap=RFT_Structs::NoSwap){
		u_int index=this->size();
		
		RFT_BUFFER_INSERT_BASIC
	}


	void append(uint64_t value,RFT_Structs::Swap swap=RFT_Structs::NoSwap){
		u_int index=this->size();
		
		RFT_BUFFER_INSERT_BASIC
	}

	void append(int64_t value,RFT_Structs::Swap swap=RFT_Structs::NoSwap){
		u_int index=this->size();
		
		RFT_BUFFER_INSERT_BASIC
	}


	void append(float value,RFT_Structs::Swap swap=RFT_Structs::NoSwap){
		u_int index=this->size();
		
		RFT_BUFFER_INSERT_BASIC
	}


	void append(double value,RFT_Structs::Swap swap=RFT_Structs::NoSwap){
		u_int index=this->size();
		
		RFT_BUFFER_INSERT_BASIC
	}


	void append(long double value,RFT_Structs::Swap swap=RFT_Structs::NoSwap){
		u_int index=this->size();
		
		RFT_BUFFER_INSERT_BASIC
	}
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
};




