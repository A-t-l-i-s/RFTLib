#pragma once
#include"require.hpp"
#include"UUID/UUID.hpp"
#include"Buffer/Buffer.hpp"





// ~~~~~~~~~~ RFT_Buffer ~~~~~~~~~~
std::ostream& operator<<(std::ostream& strm,RFT_Buffer value){
	for (u_char c:value){
		strm<<c;
	}

	return strm;
}
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



// ~~~~~~~~~~~ RFT_UUID ~~~~~~~~~~~
std::ostream& operator<<(std::ostream& strm,RFT_UUID value){

	strm<<value.finish();

	return strm;
}
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~








