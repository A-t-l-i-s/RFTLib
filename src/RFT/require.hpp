#pragma once

#define PY_SSIZE_T_CLEAN



#include<zlib.h>
#include<stdio.h>
#include<stdint.h>
#include<Python.h>

#include<map>
#include<list>
#include<chrono>
#include<thread>
#include<string>
#include<vector>
#include<fstream>
#include<iostream>
#include<algorithm>
#include<filesystem>

#include<nlohmann/json.hpp>

using std::map;
using std::list;
using std::string;
using std::vector;
using std::chrono::system_clock;

using json=nlohmann::json;
namespace fs=std::filesystem;

using namespace std::this_thread;
using namespace std::chrono_literals;



typedef unsigned char u_char;
typedef unsigned short u_short;
typedef unsigned int u_int;
typedef unsigned long u_long;
typedef unsigned long long u_long_long;



const u_char HEX_CHARS[16]={'0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'};



