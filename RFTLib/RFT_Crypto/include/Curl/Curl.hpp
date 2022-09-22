#ifndef Curl_HPP
#define Curl_HPP





CURL* Curl=curl_easy_init();
static struct curl_slist* Curl_Headers=NULL;





size_t Curl_Callback(char* ptr,size_t size,size_t mem,string* data){
	
	data->append(ptr);

	return size*mem;
}





#endif