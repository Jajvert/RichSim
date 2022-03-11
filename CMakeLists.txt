cmake_minimum_required(VERSION 3.13 FATAL_ERROR)
set(name Rich_Simplified)
project(${name} VERSION 0.1.0)
include(OpticksBuildOptions)

find_package( G4OK CONFIG REQUIRED )


file(GLOB sources src/*)
file(GLOB headers include/*)
file(GLOB RTbSrc src/RichTbDetector/*)
file(GLOB RTbInc include/RichTbDetector/*)
file(GLOB proSrc src/processes/*)
file(GLOB proInc include/processes/*)
file(GLOB localSrc src/locals/*)
file(GLOB localInc include/locals/*)

add_executable(${name} ${name}.cc ${sources} ${headers} ${RTbSrc} ${RTbInc} ${proSrc} ${proInc} ${localSrc} ${localInc} )
include_directories( ${CMAKE_CURRENT_SOURCE_DIR}/include 
                     ${CMAKE_CURRENT_SOURCE_DIR}/include/RichTbDetector 
                     ${CMAKE_CURRENT_SOURCE_DIR}/include/processes
                     ${CMAKE_CURRENT_SOURCE_DIR}/include/locals
                     ${CMAKE_CURRENT_SOURCE_DIR}/src 
                     ${CMAKE_CURRENT_SOURCE_DIR}/src/RichTbDetector 
                     ${CMAKE_CURRENT_SOURCE_DIR}/src/processes
                     ${CMAKE_CURRENT_SOURCE_DIR}/src/locals
                     )
target_link_libraries( ${name} Opticks::G4OK )
target_include_directories( ${name} PUBLIC $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include> )
target_compile_definitions( ${name} PRIVATE WITH_OPTICKS G4USE_STD11 )

install(TARGETS ${name} DESTINATION lib)
