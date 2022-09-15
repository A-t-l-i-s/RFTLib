#pragma once
#include"../require.hpp"
#include"../Core/UUID.hpp"
#include"../Core/Object.hpp"







class RFT_Volume:public RFT_Object{
protected:
// ~~~~~~~~~~~ Variables ~~~~~~~~~~
	RFT_UUID _uuid;
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



public:
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	// Constructor
	RFT_Volume(){
	}

	RFT_Volume(RFT_UUID uuid){
		this->_uuid=uuid;
	}



	// Deconstructor
	~RFT_Volume(){
	}
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



// ~~~~~~~~~~~ Operators ~~~~~~~~~~
	friend std::ostream& operator<<(std::ostream&,RFT_Volume);
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
};


