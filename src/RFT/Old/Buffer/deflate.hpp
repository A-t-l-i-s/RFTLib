#pragma once
#include"../require.hpp"
#include"Buffer.hpp"





RFT_Buffer RFT_deflate(RFT_Buffer buffer,uint8_t level=9){
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


		deflateInit(&strm,level);



		int ret;
		while (strm.avail_in!=0){
			ret=deflate(&strm,Z_NO_FLUSH);
			
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

			ret=deflate(&strm,Z_FINISH);
			
			if (ret!=Z_OK){
				outBuf.insert(outBuf.size(),chunkData,chunkSize-strm.avail_out);
				deflateEnd(&strm);
			}
		}


		free(chunkData);
	}


	return outBuf;
}



