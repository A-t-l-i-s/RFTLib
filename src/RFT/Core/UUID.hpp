#pragma once
#include"../require.hpp"
#include"Object.hpp"





class RFT_UUID:public RFT_Object{
public:
// ~~~~~~~~~~~ Variables ~~~~~~~~~~
	u_int 			timeLow=		0x00000000;
	u_short 		timeMid=		0x0000;
	u_short 		timeHigh=		0x0000;
	u_short 		clockSeq=		0x0000;
	u_long_long 	macAddress=		0x000000000000;
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	// Constructor
	RFT_UUID(){
	}

	RFT_UUID(u_int _timeLow,u_short _timeMid,u_short _timeHigh,u_short _clockSeq,u_long_long _macAddress){
		this->timeLow=_timeLow;
		this->timeMid=_timeMid;
		this->timeHigh=_timeHigh;
		this->clockSeq=_clockSeq;
		this->macAddress=_macAddress;
	}



	// Deconstructor
	~RFT_UUID(){
	}
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



// ~~~~~~~~~~~ Operators ~~~~~~~~~~
	friend std::ostream& operator<<(std::ostream&,RFT_UUID);
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
};


