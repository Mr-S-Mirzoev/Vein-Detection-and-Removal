# Structure

Structure for C++ - based code should be:

- src/ for .cpp files (sources)
- inc/ for .h/.hpp files (headers)
- scripts/ for python files (scripts)
- deps/ for dependencies

## Icons

We use icons from [this](https://icons8.com/icon/pack/free-icons/bubbles) website.

# Build driver

Build with cmake:

	cmake -B build
	make -C build

# Currently supported filters

- Equalizer (Gray and RGB)
- Median Smoothing
- Gaussian Smoothing