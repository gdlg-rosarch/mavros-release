# Script generated with Bloom
pkgdesc="ROS - MAVROS -- MAVLink extendable communication node for ROS with proxy for Ground Control Station."
url='http://wiki.ros.org/mavros'

pkgname='ros-lunar-mavros'
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
'ros-lunar-angles'
'ros-lunar-catkin'
'ros-lunar-cmake-modules'
'ros-lunar-diagnostic-msgs'
'ros-lunar-diagnostic-updater'
'ros-lunar-eigen-conversions'
'ros-lunar-geographic-msgs'
'ros-lunar-geometry-msgs'
'ros-lunar-libmavconn'
'ros-lunar-mavlink'
'ros-lunar-mavros-msgs'
'ros-lunar-nav-msgs'
'ros-lunar-pluginlib'
'ros-lunar-rosconsole-bridge'
'ros-lunar-roscpp'
'ros-lunar-sensor-msgs'
'ros-lunar-std-msgs'
'ros-lunar-std-srvs'
'ros-lunar-tf2-eigen'
'ros-lunar-tf2-ros'
)

depends=('boost'
'eigen3'
'geographiclib'
'ros-lunar-diagnostic-msgs'
'ros-lunar-diagnostic-updater'
'ros-lunar-eigen-conversions'
'ros-lunar-geographic-msgs'
'ros-lunar-geometry-msgs'
'ros-lunar-libmavconn'
'ros-lunar-mavlink'
'ros-lunar-mavros-msgs'
'ros-lunar-message-runtime'
'ros-lunar-nav-msgs'
'ros-lunar-pluginlib'
'ros-lunar-rosconsole-bridge'
'ros-lunar-roscpp'
'ros-lunar-rospy'
'ros-lunar-sensor-msgs'
'ros-lunar-std-msgs'
'ros-lunar-std-srvs'
'ros-lunar-tf2-eigen'
'ros-lunar-tf2-ros'
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
  [ -f /opt/ros/lunar/setup.bash ] && source /opt/ros/lunar/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/lunar \
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

