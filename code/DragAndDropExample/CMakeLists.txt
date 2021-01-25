cmake_minimum_required (VERSION 3.2.0)
project (DragNDrop)

set(CMAKE_CXX_STANDARD 11) # This is equal to QMAKE_CXX_FLAGS += -std=c++0x

find_package(Qt5Widgets REQUIRED)

set (DragNDropLib_src 
    ${PROJECT_SOURCE_DIR}/src/draglabel.cpp
    ${PROJECT_SOURCE_DIR}/src/dragwidget.cpp
)
set (DragNDropLib_hdr 
    ${PROJECT_SOURCE_DIR}/inc/draglabel.h
    ${PROJECT_SOURCE_DIR}/inc/dragwidget.h
)
# set (DragNDropLib_ui  ${PROJECT_SOURCE_DIR}/mainwindow.ui)
set (DragNDropBin_src ${PROJECT_SOURCE_DIR}/src/main.cpp ${PROJECT_SOURCE_DIR}/res/fridge.qrc)

qt5_wrap_cpp(DragNDropLib_hdr_moc ${DragNDropLib_hdr})
qt5_wrap_ui (DragNDropLib_ui_moc  ${DragNDropLib_ui})
qt5_add_resources(RC_SRC "res/fridge.qrc")

include_directories (${PROJECT_SOURCE_DIR}/inc)
include_directories (${PROJECT_BINARY_DIR})

add_library (DragNDropLib SHARED 
    ${DragNDropLib_src}
    ${DragNDropLib_hdr_moc}
    ${RC_SRC}
#    ${DragNDropLib_ui_moc}
)
target_link_libraries (DragNDropLib Qt5::Widgets)

add_executable(DragNDrop ${DragNDropBin_src})
target_link_libraries (DragNDrop DragNDropLib)
