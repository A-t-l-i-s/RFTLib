#ifndef Require_HPP
#define Require_HPP

#define PY_SSIZE_T_CLEAN

#include<Python.h>
#include<curl/curl.h>
#include<structmember.h>
#include<nlohmann/json.hpp>



#include<string>
#include<iostream>



using std::cout;
using std::string;
using json=nlohmann::json;



static PyObject* Module_Random;
static PyObject* Module_Hashlib;



#include<Curl/Curl.hpp>
#include<Key/Key.hpp>
#include<Module/Module.hpp>



#endif