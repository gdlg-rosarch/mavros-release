# Script generated with Bloom
pkgdesc="ROS - MAVROS -- MAVLink extendable communication node for ROS with proxy for Ground Control Station."
url='http://wiki.ros.org/mavros'

pkgname='ros-kinetic-mavros'
pkgver='0.24.0_1'
pkgrel=1
arch=('any')
license=('GPLv3'
'LGPLv3'
'BSD'
)

makedepends=('boost'
'eigen3'
'geographiclib'
'gtest'
'ros-kinetic-angles'
'ros-kinetic-catkin'
'ros-kinetic-cmake-modules'
'ros-kinetic-diagnostic-msgs'
'ros-kinetic-diagnostic-updater'
'ros-kinetic-eigen-conversions'
'ros-kinetic-geographic-msgs'
'ros-kinetic-geometry-msgs'
'ros-kinetic-libmavconn'
'ros-kinetic-mavlink'
'ros-kinetic-mavros-msgs'
'ros-kinetic-nav-msgs'
'ros-kinetic-pluginlib'
'ros-kinetic-rosconsole-bridge'
'ros-kinetic-roscpp'
'ros-kinetic-sensor-msgs'
'ros-kinetic-std-msgs'
'ros-kinetic-std-srvs'
'ros-kinetic-tf2-eigen'
'ros-kinetic-tf2-ros'
)

depends=('boost'
'eigen3'
'geographiclib'
'ros-kinetic-diagnostic-msgs'
'ros-kinetic-diagnostic-updater'
'ros-kinetic-eigen-conversions'
'ros-kinetic-geographic-msgs'
'ros-kinetic-geometry-msgs'
'ros-kinetic-libmavconn'
'ros-kinetic-mavlink'
'ros-kinetic-mavros-msgs'
'ros-kinetic-message-runtime'
'ros-kinetic-nav-msgs'
'ros-kinetic-pluginlib'
'ros-kinetic-rosconsole-bridge'
'ros-kinetic-roscpp'
'ros-kinetic-rospy'
'ros-kinetic-sensor-msgs'
'ros-kinetic-std-msgs'
'ros-kinetic-std-srvs'
'ros-kinetic-tf2-eigen'
'ros-kinetic-tf2-ros'
)

conflicts=()
replaces=()

_dir=mavros
source=()
md5sums=()

prepare() {
    cp -R $startdir/mavros $srcdir/mavros
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

