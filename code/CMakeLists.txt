cmake_minimum_required (VERSION 3.2.0)
project (MyProject)

set(CMAKE_CXX_STANDARD 11) # This is equal to QMAKE_CXX_FLAGS += -std=c++0x

find_package(Qt5Widgets REQUIRED)

set (MyProjectLib_src 
    ${PROJECT_SOURCE_DIR}/src/addressbook.cpp
    ${PROJECT_SOURCE_DIR}/src/finddialog.cpp
)
set (MyProjectLib_hdr 
    ${PROJECT_SOURCE_DIR}/inc/addressbook.h
    ${PROJECT_SOURCE_DIR}/inc/finddialog.h
)
# set (MyProjectLib_ui  ${PROJECT_SOURCE_DIR}/mainwindow.ui)
set (MyProjectBin_src ${PROJECT_SOURCE_DIR}/src/main.cpp)

qt5_wrap_cpp(MyProjectLib_hdr_moc ${MyProjectLib_hdr})
qt5_wrap_ui (MyProjectLib_ui_moc  ${MyProjectLib_ui})

include_directories (${PROJECT_SOURCE_DIR}/inc)
include_directories (${PROJECT_BINARY_DIR})

add_library (MyProjectLib SHARED 
    ${MyProjectLib_src}
    ${MyProjectLib_hdr_moc}
#    ${MyProjectLib_ui_moc}
)
target_link_libraries (MyProjectLib Qt5::Widgets)

add_executable(MyProject ${MyProjectBin_src})
target_link_libraries (MyProject MyProjectLib)
