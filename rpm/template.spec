Name:           ros-jade-libmavconn
Version:        0.16.5
Release:        0%{?dist}
Summary:        ROS libmavconn package

Group:          Development/Libraries
License:        GPLv3
URL:            http://wiki.ros.org/mavros
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       console-bridge-devel
Requires:       ros-jade-mavlink
BuildRequires:  boost-devel
BuildRequires:  console-bridge-devel
BuildRequires:  gtest-devel
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-mavlink

%description
MAVLink communication library. This library provide unified connection handling
classes and URL to connection object mapper. This library can be used in
standalone programs.

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
* Mon Jan 11 2016 Vladimir Ermakov <vooon341@gmail.com> - 0.16.5-0
- Autogenerated by Bloom

* Mon Dec 14 2015 Vladimir Ermakov <vooon341@gmail.com> - 0.16.4-0
- Autogenerated by Bloom

* Thu Nov 19 2015 Vladimir Ermakov <vooon341@gmail.com> - 0.16.3-0
- Autogenerated by Bloom

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

* Wed Jul 01 2015 Vladimir Ermakov <vooon341@gmail.com> - 0.12.0-0
- Autogenerated by Bloom

* Sun Apr 26 2015 Vladimir Ermakov <vooon341@gmail.com> - 0.11.2-0
- Autogenerated by Bloom

* Mon Apr 06 2015 Vladimir Ermakov <vooon341@gmail.com> - 0.11.1-0
- Autogenerated by Bloom

* Tue Mar 24 2015 Vladimir Ermakov <vooon341@gmail.com> - 0.11.0-0
- Autogenerated by Bloom

* Wed Feb 25 2015 Vladimir Ermakov <vooon341@gmail.com> - 0.10.2-0
- Autogenerated by Bloom

