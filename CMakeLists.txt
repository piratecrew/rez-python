CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)


# ------------------------------------------------------------------------------
# Build Dependencies to build all standard modules
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

ExternalProject_add(
    python
    URL http://www.python.org/ftp/python/${python_version}/Python-${python_version}.tgz
    PREFIX python
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ./configure --prefix=${CMAKE_INSTALL_PREFIX} --enable-shared --enable-ipv6 --enable-unicode=ucs4
    INSTALL_COMMAND make install VERBOSE=1
    ALWAYS 1
    BUILD_COMMAND make -j$ENV{REZ_BUILD_THREAD_COUNT} VERBOSE=1
    BUILD_IN_SOURCE 1
)

install(
    FILES cmake/FindPython.cmake cmake/python.cmake
    DESTINATION cmake
)