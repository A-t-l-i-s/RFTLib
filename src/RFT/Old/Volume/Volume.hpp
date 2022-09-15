#pragma once
#include"../require.hpp"
#include"../UUID/UUID.hpp"
#include"../Buffer/Block.hpp"





class RFT_Volume{
protected:
// ~~~~~~~~~~~ Variables ~~~~~~~~~~
	std::fstream _stream;

	RFT_UUID _uuid;

	u_int _blockSize=512;
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



public:
// ~~~ Constructor/Deconstructor ~~
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
	void setBlockSize(u_int blockSize){
		this->_blockSize=blockSize;
	}

	u_int getBlockSize(){
		return this->_blockSize;
	}
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



// ~~~~~~~~~ IO Functions ~~~~~~~~~
	void open(){
		RFT_Buffer b;
		b.insert(0,"\\\\?\\Volume");
		b.insert(b.size(),this->_uuid.finish());

		this->_stream.open(
			b.asString(),
			std::ios::in | std::ios::out | std::ios::binary
		);
	}



	bool isOpen(){
		return this->_stream.is_open();
	}


	bool eof(){
		return this->_stream.eof();
	}

	bool good(){
		return this->_stream.good();
	}
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



// ~~~~~~~~~~~~ Blocks ~~~~~~~~~~~~
	RFT_Block allocateBlock(){
		RFT_Block block(this->_blockSize);
		return block;
	}



	void readBlock(RFT_Block* block){
		this->_stream.read(
			(char*)block->data(),
			this->_blockSize
		);
	}



	void writeBlock(RFT_Block* block){
		this->_stream.write(
			(char*)block->data(),
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



	void setBlock(u_int index){
		this->_stream.seekg(
			index*this->_blockSize,
			std::ios::beg
		);
	}
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
};


