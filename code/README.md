# Structure

Structure for C++ - based code should be:

- src/ for .cpp files (sources)
- inc/ for .h/.hpp files (headers)
- scripts/ for python files (scripts)
- deps/ for dependencies

# Build driver

Build with cmake:

	cmake -B build
	make -C build

# Currently supported filters