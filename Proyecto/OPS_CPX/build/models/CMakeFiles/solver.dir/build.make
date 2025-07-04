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
include models/CMakeFiles/solver.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include models/CMakeFiles/solver.dir/compiler_depend.make

# Include the progress variables for this target.
include models/CMakeFiles/solver.dir/progress.make

# Include the compile flags for this target's objects.
include models/CMakeFiles/solver.dir/flags.make

models/CMakeFiles/solver.dir/src/OPS_bc1.cpp.o: models/CMakeFiles/solver.dir/flags.make
models/CMakeFiles/solver.dir/src/OPS_bc1.cpp.o: /home/kilian/Escritorio/TFG/Proyecto/OPS_CPX/src/models/src/OPS_bc1.cpp
models/CMakeFiles/solver.dir/src/OPS_bc1.cpp.o: models/CMakeFiles/solver.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/kilian/Escritorio/TFG/Proyecto/OPS_CPX/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object models/CMakeFiles/solver.dir/src/OPS_bc1.cpp.o"
	cd /home/kilian/Escritorio/TFG/Proyecto/OPS_CPX/build/models && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT models/CMakeFiles/solver.dir/src/OPS_bc1.cpp.o -MF CMakeFiles/solver.dir/src/OPS_bc1.cpp.o.d -o CMakeFiles/solver.dir/src/OPS_bc1.cpp.o -c /home/kilian/Escritorio/TFG/Proyecto/OPS_CPX/src/models/src/OPS_bc1.cpp

models/CMakeFiles/solver.dir/src/OPS_bc1.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/solver.dir/src/OPS_bc1.cpp.i"
	cd /home/kilian/Escritorio/TFG/Proyecto/OPS_CPX/build/models && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/kilian/Escritorio/TFG/Proyecto/OPS_CPX/src/models/src/OPS_bc1.cpp > CMakeFiles/solver.dir/src/OPS_bc1.cpp.i

models/CMakeFiles/solver.dir/src/OPS_bc1.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/solver.dir/src/OPS_bc1.cpp.s"
	cd /home/kilian/Escritorio/TFG/Proyecto/OPS_CPX/build/models && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/kilian/Escritorio/TFG/Proyecto/OPS_CPX/src/models/src/OPS_bc1.cpp -o CMakeFiles/solver.dir/src/OPS_bc1.cpp.s

# Object files for target solver
solver_OBJECTS = \
"CMakeFiles/solver.dir/src/OPS_bc1.cpp.o"

# External object files for target solver
solver_EXTERNAL_OBJECTS =

models/libsolver.a: models/CMakeFiles/solver.dir/src/OPS_bc1.cpp.o
models/libsolver.a: models/CMakeFiles/solver.dir/build.make
models/libsolver.a: models/CMakeFiles/solver.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/kilian/Escritorio/TFG/Proyecto/OPS_CPX/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX static library libsolver.a"
	cd /home/kilian/Escritorio/TFG/Proyecto/OPS_CPX/build/models && $(CMAKE_COMMAND) -P CMakeFiles/solver.dir/cmake_clean_target.cmake
	cd /home/kilian/Escritorio/TFG/Proyecto/OPS_CPX/build/models && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/solver.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
models/CMakeFiles/solver.dir/build: models/libsolver.a
.PHONY : models/CMakeFiles/solver.dir/build

models/CMakeFiles/solver.dir/clean:
	cd /home/kilian/Escritorio/TFG/Proyecto/OPS_CPX/build/models && $(CMAKE_COMMAND) -P CMakeFiles/solver.dir/cmake_clean.cmake
.PHONY : models/CMakeFiles/solver.dir/clean

models/CMakeFiles/solver.dir/depend:
	cd /home/kilian/Escritorio/TFG/Proyecto/OPS_CPX/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/kilian/Escritorio/TFG/Proyecto/OPS_CPX/src /home/kilian/Escritorio/TFG/Proyecto/OPS_CPX/src/models /home/kilian/Escritorio/TFG/Proyecto/OPS_CPX/build /home/kilian/Escritorio/TFG/Proyecto/OPS_CPX/build/models /home/kilian/Escritorio/TFG/Proyecto/OPS_CPX/build/models/CMakeFiles/solver.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : models/CMakeFiles/solver.dir/depend

