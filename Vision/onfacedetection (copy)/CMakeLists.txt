cmake_minimum_required(VERSION 2.8)
project(onfacedetection)
find_package(qibuild)

option(ONMARKDETECTION_IS_REMOTE
  "module is compiled as a remote module (ON or OFF)"
  ON)

set(_srcs
  main.cpp
  onfacedetection.h
  onfacedetection.cpp
)

if(ONMARKDETECTION_IS_REMOTE)
  add_definitions(" -DONMARKDETECTION_IS_REMOTE ")
  qi_create_bin(onfacedetection ${_srcs})
else()
  qi_create_lib(onfacedetection SHARED ${_srcs} SUBFOLDER naoqi)
endif()

qi_use_lib(onfacedetection ALCOMMON ALPROXIES ALTHREAD)
