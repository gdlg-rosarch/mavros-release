# Script generated with Bloom
pkgdesc="ROS - Extra nodes and plugins for <a href="http://wiki.ros.org/mavros">MAVROS</a>."
url='http://wiki.ros.org/mavros_extras'

pkgname='ros-kinetic-mavros-extras'
pkgver='0.24.0_1'
pkgrel=1
arch=('any')
license=('GPLv3'
'LGPLv3'
'BSD'
)

makedepends=('ros-kinetic-catkin'
'ros-kinetic-cmake-modules'
'ros-kinetic-geometry-msgs'
'ros-kinetic-mavros'
'ros-kinetic-mavros-msgs'
'ros-kinetic-roscpp'
'ros-kinetic-sensor-msgs'
'ros-kinetic-std-msgs'
'ros-kinetic-tf'
'ros-kinetic-urdf'
'ros-kinetic-visualization-msgs'
)

depends=('ros-kinetic-geometry-msgs'
'ros-kinetic-mavros'
'ros-kinetic-mavros-msgs'
'ros-kinetic-roscpp'
'ros-kinetic-sensor-msgs'
'ros-kinetic-std-msgs'
'ros-kinetic-tf'
'ros-kinetic-urdf'
'ros-kinetic-visualization-msgs'
)

conflicts=()
replaces=()

_dir=mavros_extras
source=()
md5sums=()

prepare() {
    cp -R $startdir/mavros_extras $srcdir/mavros_extras
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

