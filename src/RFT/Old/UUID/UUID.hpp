#pragma once
#include"../require.hpp"
#include"../Buffer/Buffer.hpp"





class RFT_UUID{
public:
// ~~~~~~~~~~~ Variables ~~~~~~~~~~
	u_int 			timeLow=		0x00000000;
	u_short 		timeMid=		0x0000;
	u_short 		timeHigh=		0x0000;
	u_short 		clockSeq=		0x0000;
	u_long_long 	macAddress=		0x000000000000;
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



// ~~~ Constructor/Deconstructor ~~
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



// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	RFT_Buffer finish(){
		RFT_Buffer out, buf, hex;

		out.insert(out.size(),"{");


		buf.setValue(this->timeLow);

		hex=buf.asHex();
		out.insert(out.size(),hex);
		out.insert(out.size(),"-");



		buf.setValue(this->timeMid);

		hex=buf.asHex();
		out.insert(out.size(),hex);
		out.insert(out.size(),"-");



		buf.setValue(this->timeHigh);

		hex=buf.asHex();
		out.insert(out.size(),hex);
		out.insert(out.size(),"-");



		buf.setValue(this->clockSeq);

		hex=buf.asHex();
		out.insert(out.size(),hex);
		out.insert(out.size(),"-");



		buf.setValue(this->macAddress);
		buf.resize(6);

		hex=buf.asHex();
		out.insert(out.size(),hex);
		out.insert(out.size(),"}");

		return out;
	}
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



// ~~~~~~~~~~~ Operators ~~~~~~~~~~
	friend std::ostream& operator<<(std::ostream&,RFT_UUID);
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
};


