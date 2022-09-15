#pragma once
#include"../require.hpp"
#include"Buffer.hpp"





#define TO_BUF_BASIC 				\
	u_int size=sizeof(value);		\
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






RFT_Buffer int8ToBuf(int8_t value){
	TO_BUF_SINGLE
}

RFT_Buffer uint8ToBuf(uint8_t value){
	TO_BUF_SINGLE
}



RFT_Buffer boolToBuf(bool value){
	TO_BUF_SINGLE
}



RFT_Buffer pointerToBuf(void* value,bool reversed=false){
	TO_BUF_BASIC
}



RFT_Buffer int16ToBuf(int16_t value,bool reversed=false){
	TO_BUF_BASIC
}

RFT_Buffer uint16ToBuf(uint16_t value,bool reversed=false){
	TO_BUF_BASIC
}



RFT_Buffer int32ToBuf(int32_t value,bool reversed=false){
	TO_BUF_BASIC
}

RFT_Buffer uint32ToBuf(uint32_t value,bool reversed=false){
	TO_BUF_BASIC
}



RFT_Buffer int64ToBuf(int64_t value,bool reversed=false){
	TO_BUF_BASIC
}

RFT_Buffer uint64ToBuf(uint64_t value,bool reversed=false){
	TO_BUF_BASIC
}



RFT_Buffer floatToBuf(float value,bool reversed=false){
	TO_BUF_BASIC
}



RFT_Buffer doubleToBuf(double value,bool reversed=false){
	TO_BUF_BASIC
}



RFT_Buffer longDoubleToBuf(long double value,bool reversed=false){
	TO_BUF_BASIC
}

