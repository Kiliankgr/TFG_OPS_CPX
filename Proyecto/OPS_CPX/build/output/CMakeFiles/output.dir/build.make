# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.22

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/kilian/Escritorio/TFG/Proyecto/OPS_CPX/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/kilian/Escritorio/TFG/Proyecto/OPS_CPX/build

# Include any dependencies generated for this target.
include output/CMakeFiles/output.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include output/CMakeFiles/output.dir/compiler_depend.make

# Include the progress variables for this target.
include output/CMakeFiles/output.dir/progress.make

# Include the compile flags for this target's objects.
include output/CMakeFiles/output.dir/flags.make

output/CMakeFiles/output.dir/src/OPS_output_t.cpp.o: output/CMakeFiles/output.dir/flags.make
output/CMakeFiles/output.dir/src/OPS_output_t.cpp.o: /home/kilian/Escritorio/TFG/Proyecto/OPS_CPX/src/output/src/OPS_output_t.cpp
output/CMakeFiles/output.dir/src/OPS_output_t.cpp.o: output/CMakeFiles/output.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/kilian/Escritorio/TFG/Proyecto/OPS_CPX/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object output/CMakeFiles/output.dir/src/OPS_output_t.cpp.o"
	cd /home/kilian/Escritorio/TFG/Proyecto/OPS_CPX/build/output && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT output/CMakeFiles/output.dir/src/OPS_output_t.cpp.o -MF CMakeFiles/output.dir/src/OPS_output_t.cpp.o.d -o CMakeFiles/output.dir/src/OPS_output_t.cpp.o -c /home/kilian/Escritorio/TFG/Proyecto/OPS_CPX/src/output/src/OPS_output_t.cpp

output/CMakeFiles/output.dir/src/OPS_output_t.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/output.dir/src/OPS_output_t.cpp.i"
	cd /home/kilian/Escritorio/TFG/Proyecto/OPS_CPX/build/output && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/kilian/Escritorio/TFG/Proyecto/OPS_CPX/src/output/src/OPS_output_t.cpp > CMakeFiles/output.dir/src/OPS_output_t.cpp.i

output/CMakeFiles/output.dir/src/OPS_output_t.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/output.dir/src/OPS_output_t.cpp.s"
	cd /home/kilian/Escritorio/TFG/Proyecto/OPS_CPX/build/output && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/kilian/Escritorio/TFG/Proyecto/OPS_CPX/src/output/src/OPS_output_t.cpp -o CMakeFiles/output.dir/src/OPS_output_t.cpp.s

# Object files for target output
output_OBJECTS = \
"CMakeFiles/output.dir/src/OPS_output_t.cpp.o"

# External object files for target output
output_EXTERNAL_OBJECTS =

output/liboutput.a: output/CMakeFiles/output.dir/src/OPS_output_t.cpp.o
output/liboutput.a: output/CMakeFiles/output.dir/build.make
output/liboutput.a: output/CMakeFiles/output.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/kilian/Escritorio/TFG/Proyecto/OPS_CPX/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX static library liboutput.a"
	cd /home/kilian/Escritorio/TFG/Proyecto/OPS_CPX/build/output && $(CMAKE_COMMAND) -P CMakeFiles/output.dir/cmake_clean_target.cmake
	cd /home/kilian/Escritorio/TFG/Proyecto/OPS_CPX/build/output && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/output.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
output/CMakeFiles/output.dir/build: output/liboutput.a
.PHONY : output/CMakeFiles/output.dir/build

output/CMakeFiles/output.dir/clean:
	cd /home/kilian/Escritorio/TFG/Proyecto/OPS_CPX/build/output && $(CMAKE_COMMAND) -P CMakeFiles/output.dir/cmake_clean.cmake
.PHONY : output/CMakeFiles/output.dir/clean

output/CMakeFiles/output.dir/depend:
	cd /home/kilian/Escritorio/TFG/Proyecto/OPS_CPX/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/kilian/Escritorio/TFG/Proyecto/OPS_CPX/src /home/kilian/Escritorio/TFG/Proyecto/OPS_CPX/src/output /home/kilian/Escritorio/TFG/Proyecto/OPS_CPX/build /home/kilian/Escritorio/TFG/Proyecto/OPS_CPX/build/output /home/kilian/Escritorio/TFG/Proyecto/OPS_CPX/build/output/CMakeFiles/output.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : output/CMakeFiles/output.dir/depend

