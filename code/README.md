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

# Current state

code/
├── deps
│   └── Mask_RCNN - Mask RCNN library (old, bug-having version)
├── localizer.py - Haven't tested yet
├── README.md
└── src
    └── shape_detection.cpp - Shape detector (TO REMOVE: not suitable for our studies)

11 directories, 78 files