#pragma once
#include"require.hpp"
#include"Core/Object.hpp"
#include"Array/Buffer.hpp"
#include"Array/Vector.hpp"





// ~~~~~~~~~~ RFT_Object ~~~~~~~~~~
	std::ostream& operator<<(std::ostream& strm,RFT_Object value){
		strm<<std::hex<<&value;

		return strm;
	}
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



// ~~~~~~~~~~ RFT_Buffer ~~~~~~~~~~
	std::ostream& operator<<(std::ostream& strm,RFT_Buffer value){
		for (u_char c:value){
			strm<<c;
		}

		return strm;
	}
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



// ~~~~~~~~~~ RFT_Vector ~~~~~~~~~~
	std::ostream& operator<<(std::ostream& strm,RFT_Vector value){
		for (u_char c:value){
			strm<<c;
		}

		return strm;
	}
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~