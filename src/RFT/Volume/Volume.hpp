#pragma once
#include"../require.hpp"
#include"../Core/UUID.hpp"
#include"../Core/Object.hpp"
#include"../Array/Buffer.hpp"







class RFT_Volume:public RFT_Object{
protected:
// ~~~~~~~~~~~ Variables ~~~~~~~~~~
	std::fstream _stream;
	u_int _blockSize=512;

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



// ~~~~~~~~~~~ Functions ~~~~~~~~~~
	RFT_UUID getUUID(){
		return this->_uuid;
	}

	void setUUID(RFT_UUID uuid){
		this->_uuid=uuid;
	}



	void setBlockSize(u_int blockSize){
		this->_blockSize=blockSize;
	}

	u_int getBlockSize(){
		return this->_blockSize;
	}
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



// ~~~~~~~~~ IO Functions ~~~~~~~~~
	bool open(){
		RFT_Vector b;

		b.append((u_char*)"\\\\?\\Volume",10);
		b.append(this->_uuid.finish());


		this->_stream.open(
			b.asString(),
			std::ios::in | std::ios::out | std::ios::binary
		);


		return this->isOpen();
	}



	bool close(){
		if (this->isOpen()){
			this->_stream.close();

			return true;
		} else {
			return false;
		}
	}



	bool isOpen(){
		return this->_stream.is_open();
	}



	bool eof(){
		return this->_stream.eof();
	}

	bool good(){
		if (this->isOpen()){
			return this->_stream.good();
		} else {
			return false;
		}
	}
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



// ~~~~~~~~~~~~ Blocks ~~~~~~~~~~~~
	RFT_Buffer readBlock(){
		RFT_Buffer block(this->_blockSize);

		this->_stream.read(
			(char*)block.data(),
			this->_blockSize
		);

		return block;
	}



	void writeBlock(RFT_Buffer block){
		this->_stream.write(
			(char*)block.data(),
			this->_blockSize
		);
	}



	void nextBlock(){
		this->_stream.seekg(
			this->_blockSize,
			std::ios::cur
		);
	}



	void prevBlock(){
		this->_stream.seekg(
			-this->_blockSize,
			std::ios::cur
		);
	}



	void seekBlock(u_int index){
		this->_stream.seekg(
			index*this->_blockSize,
			std::ios::beg
		);
	}



	u_int tellBlock(){
		return this->_stream.tellg()/this->_blockSize;
	}
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
};


