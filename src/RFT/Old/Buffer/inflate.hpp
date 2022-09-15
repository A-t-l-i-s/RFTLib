#pragma once
#include"../require.hpp"
#include"Buffer.hpp"





RFT_Buffer RFT_inflate(RFT_Buffer buffer){
	RFT_Buffer outBuf;


	u_int chunkSize=buffer.size();

	if (chunkSize>0){
	
		u_char* chunkData=new u_char[chunkSize];

		
		z_stream strm;

		strm.zalloc=Z_NULL;
		strm.zfree=Z_NULL;
		strm.opaque=Z_NULL;

		strm.next_in=buffer.data();
		strm.avail_in=buffer.size();
		strm.next_out=chunkData;
		strm.avail_out=chunkSize;


		inflateInit(&strm);



		int ret=Z_OK;
		while (ret==Z_OK){
			ret=inflate(&strm,Z_NO_FLUSH);

			if (strm.avail_out==0){
				outBuf.insert(outBuf.size(),chunkData,chunkSize);
			

				strm.next_out=chunkData;
				strm.avail_out=chunkSize;
			}
		}


		

		ret=Z_OK;
		while (ret==Z_OK){
			if (strm.avail_out==0){
				outBuf.insert(outBuf.size(),chunkData,chunkSize);

				strm.next_out=chunkData;
				strm.avail_out=chunkSize;
			}

			ret=inflate(&strm,Z_FINISH);
			
			if (ret!=Z_OK){
				outBuf.insert(outBuf.size(),chunkData,chunkSize-strm.avail_out);
				inflateEnd(&strm);
			}

		}


		free(chunkData);
	}


	return outBuf;
}




