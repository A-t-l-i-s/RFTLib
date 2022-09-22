#pragma once
#include"../require.hpp"
#include"Object.hpp"
#include"../Array/toBuf.hpp"
#include"../Array/Buffer.hpp"





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



// ~~~~~~~~~~~ Functions ~~~~~~~~~~
	RFT_Buffer finish(bool upper=false){
		RFT_Buffer buf(38), temp;


		buf.set(0,'{');

		buf.set(9,'-');
		buf.set(14,'-');
		buf.set(19,'-');
		buf.set(24,'-');


		temp=uint32ToBuf(this->timeLow);
		temp=temp.asHex();
		buf.assign(1,temp);


		temp=uint16ToBuf(this->timeMid);
		temp=temp.asHex();
		buf.assign(10,temp);


		temp=uint16ToBuf(this->timeHigh);
		temp=temp.asHex();
		buf.assign(15,temp);


		temp=uint16ToBuf(this->clockSeq);
		temp=temp.asHex();
		buf.assign(20,temp);


		temp=uint48ToBuf(this->macAddress);
		temp=temp.asHex();
		buf.assign(25,temp);


		buf.set(37,'}');


		temp.free();


		return buf;
	}
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
};


