Name:           ros-indigo-mavros-msgs
Version:        0.16.4
Release:        0%{?dist}
Summary:        ROS mavros_msgs package

Group:          Development/Libraries
License:        GPLv3
URL:            http://wiki.ros.org/mavros_msgs
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-message-runtime
Requires:       ros-indigo-std-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-std-msgs

%description
mavros_msgs defines messages for MAVROS.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
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

