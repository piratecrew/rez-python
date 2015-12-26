CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

# ------------------------------------------------------------------------------
# Build Dependencies
#
# Centos:
# yum groupinstall 'Development Tools'
# yum install zlib-devel
# yum install readline-devel
# yum install ncurses-devel
# yum install openssl-devel
# yum install gdbm-devel
# yum install sqlite-devel
# yum install bzip2-devel
# ------------------------------------------------------------------------------


set(python_version $ENV{REZ_BUILD_PROJECT_VERSION})

set(url_python http://www.python.org/ftp/python/${python_version}/Python-${python_version}.tgz)

set(make_args -j$ENV{REZ_BUILD_THREAD_COUNT} VERBOSE=1)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    python
    URL ${url_python}
    PREFIX python
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ./configure --prefix=${CMAKE_INSTALL_PREFIX} --enable-shared --enable-unicode=ucs4
    INSTALL_COMMAND "${install_cmd}"
    BUILD_IN_SOURCE 1
    BUILD_COMMAND make ${make_args}
)

rez_install_files(
    cmake/python.cmake
    DESTINATION .
)
