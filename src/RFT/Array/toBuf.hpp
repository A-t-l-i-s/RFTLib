#pragma once
#include"../require.hpp"
#include"Buffer.hpp"





#define TO_BUF_BASIC 				\
	u_char* buf=(u_char*)&value;	\
									\
	RFT_Buffer buffer(size);		\
	buffer.assign(0,buf,size);		\
									\
	if (reversed)					\
		buffer.reverse();			\
									\
	return buffer;					\



#define TO_BUF_SINGLE 				\
	RFT_Buffer buffer(1);			\
									\
	buffer.set(0,value);			\
									\
	return buffer;					\







// Bool to Buffer
RFT_Buffer boolToBuf(bool value){
	TO_BUF_SINGLE
}



// Void Pointer to Buffer
RFT_Buffer pointerToBuf(void* value,bool reversed=false){
	u_int size=sizeof(value);
	TO_BUF_BASIC
}



// Int8 to Buffer
RFT_Buffer int8ToBuf(int8_t value){
	TO_BUF_SINGLE
}

RFT_Buffer uint8ToBuf(uint8_t value){
	TO_BUF_SINGLE
}



// Int16 to Buffer
RFT_Buffer int16ToBuf(int16_t value,bool reversed=false){
	u_int size=2;
	TO_BUF_BASIC
}

RFT_Buffer uint16ToBuf(uint16_t value,bool reversed=false){
	u_int size=2;
	TO_BUF_BASIC
}



// Int24 to Buffer
RFT_Buffer int24ToBuf(int32_t value,bool reversed=false){
	u_int size=3;
	TO_BUF_BASIC
}

RFT_Buffer uint24ToBuf(uint32_t value,bool reversed=false){
	u_int size=3;
	TO_BUF_BASIC
}



// Int32 to Buffer
RFT_Buffer int32ToBuf(int32_t value,bool reversed=false){
	u_int size=4;
	TO_BUF_BASIC
}

RFT_Buffer uint32ToBuf(uint32_t value,bool reversed=false){
	u_int size=4;
	TO_BUF_BASIC
}



// Int40 to Buffer
RFT_Buffer int40ToBuf(int64_t value,bool reversed=false){
	u_int size=5;
	TO_BUF_BASIC
}

RFT_Buffer uint40ToBuf(uint64_t value,bool reversed=false){
	u_int size=5;
	TO_BUF_BASIC
}



// Int48 to Buffer
RFT_Buffer int48ToBuf(int64_t value,bool reversed=false){
	u_int size=6;
	TO_BUF_BASIC
}

RFT_Buffer uint48ToBuf(uint64_t value,bool reversed=false){
	u_int size=6;
	TO_BUF_BASIC
}



// Int56 to Buffer
RFT_Buffer int56ToBuf(int64_t value,bool reversed=false){
	u_int size=7;
	TO_BUF_BASIC
}

RFT_Buffer uint56ToBuf(uint64_t value,bool reversed=false){
	u_int size=7;
	TO_BUF_BASIC
}



// Int64 to Buffer
RFT_Buffer int64ToBuf(int64_t value,bool reversed=false){
	u_int size=8;
	TO_BUF_BASIC
}

RFT_Buffer uint64ToBuf(uint64_t value,bool reversed=false){
	u_int size=8;
	TO_BUF_BASIC
}



// Float to Buffer
RFT_Buffer floatToBuf(float value,bool reversed=false){
	u_int size=4;
	TO_BUF_BASIC
}



// Double to Buffer
RFT_Buffer doubleToBuf(double value,bool reversed=false){
	u_int size=8;
	TO_BUF_BASIC
}



// Long Double to Buffer
RFT_Buffer longDoubleToBuf(long double value,bool reversed=false){
	u_int size=16;
	TO_BUF_BASIC
}

