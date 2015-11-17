Name:           ros-jade-test-mavros
Version:        0.16.2
Release:        0%{?dist}
Summary:        ROS test_mavros package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       eigen3-devel
Requires:       ros-jade-control-toolbox
Requires:       ros-jade-eigen-conversions
Requires:       ros-jade-geometry-msgs
Requires:       ros-jade-mavros
Requires:       ros-jade-mavros-extras
Requires:       ros-jade-roscpp
Requires:       ros-jade-std-msgs
Requires:       ros-jade-tf2-ros
BuildRequires:  eigen3-devel
BuildRequires:  ros-jade-angles
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-cmake-modules
BuildRequires:  ros-jade-control-toolbox
BuildRequires:  ros-jade-eigen-conversions
BuildRequires:  ros-jade-geometry-msgs
BuildRequires:  ros-jade-mavros
BuildRequires:  ros-jade-mavros-extras
BuildRequires:  ros-jade-roscpp
BuildRequires:  ros-jade-std-msgs
BuildRequires:  ros-jade-tf2-ros

%description
Tests for MAVROS package

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Tue Nov 17 2015 Vladimir Ermakov <vooon341@gmail.com> - 0.16.2-0
- Autogenerated by Bloom

* Fri Nov 13 2015 Vladimir Ermakov <vooon341@gmail.com> - 0.16.1-0
- Autogenerated by Bloom

* Mon Nov 09 2015 Vladimir Ermakov <vooon341@gmail.com> - 0.16.0-0
- Autogenerated by Bloom

* Thu Sep 17 2015 Vladimir Ermakov <vooon341@gmail.com> - 0.15.0-0
- Autogenerated by Bloom

* Thu Aug 20 2015 Vladimir Ermakov <vooon341@gmail.com> - 0.14.2-0
- Autogenerated by Bloom

* Wed Aug 19 2015 Vladimir Ermakov <vooon341@gmail.com> - 0.14.1-0
- Autogenerated by Bloom

* Mon Aug 17 2015 Vladimir Ermakov <vooon341@gmail.com> - 0.14.0-0
- Autogenerated by Bloom

* Wed Aug 05 2015 Vladimir Ermakov <vooon341@gmail.com> - 0.13.1-0
- Autogenerated by Bloom

* Sat Aug 01 2015 Vladimir Ermakov <vooon341@gmail.com> - 0.13.0-0
- Autogenerated by Bloom

