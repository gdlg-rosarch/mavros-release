Name:           ros-hydro-mavros
Version:        0.7.0
Release:        0%{?dist}
Summary:        ROS mavros package

Group:          Development/Libraries
License:        GPLv3
URL:            http://wiki.ros.org/mavros
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       ros-hydro-angles
Requires:       ros-hydro-diagnostic-msgs
Requires:       ros-hydro-diagnostic-updater
Requires:       ros-hydro-geometry-msgs
Requires:       ros-hydro-mavlink
Requires:       ros-hydro-message-runtime
Requires:       ros-hydro-pluginlib
Requires:       ros-hydro-roscpp
Requires:       ros-hydro-rospy
Requires:       ros-hydro-sensor-msgs
Requires:       ros-hydro-std-msgs
Requires:       ros-hydro-tf
BuildRequires:  boost-devel
BuildRequires:  gtest-devel
BuildRequires:  ros-hydro-angles
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-diagnostic-msgs
BuildRequires:  ros-hydro-diagnostic-updater
BuildRequires:  ros-hydro-geometry-msgs
BuildRequires:  ros-hydro-mavlink
BuildRequires:  ros-hydro-message-generation
BuildRequires:  ros-hydro-pluginlib
BuildRequires:  ros-hydro-roscpp
BuildRequires:  ros-hydro-rospy
BuildRequires:  ros-hydro-sensor-msgs
BuildRequires:  ros-hydro-std-msgs
BuildRequires:  ros-hydro-tf

%description
MAVROS -- MAVLink extendable communication node for ROS with UDP proxy for
Ground Control Station.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Tue Aug 12 2014 Vladimir Ermakov <vooon341@gmail.com> - 0.7.0-0
- Autogenerated by Bloom

