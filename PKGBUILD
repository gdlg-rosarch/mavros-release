# Script generated with Bloom
pkgdesc="ROS - MAVLink communication library. This library provide unified connection handling classes and URL to connection object mapper. This library can be used in standalone programs."
url='http://wiki.ros.org/mavros'

pkgname='ros-kinetic-libmavconn'
pkgver='0.24.0_1'
pkgrel=1
arch=('any')
license=('GPLv3'
'LGPLv3'
'BSD'
)

makedepends=('boost'
'console-bridge'
'gtest'
'ros-kinetic-catkin'
'ros-kinetic-mavlink'
)

depends=('boost'
'console-bridge'
'ros-kinetic-mavlink'
)

conflicts=()
replaces=()

_dir=libmavconn
source=()
md5sums=()

prepare() {
    cp -R $startdir/libmavconn $srcdir/libmavconn
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

