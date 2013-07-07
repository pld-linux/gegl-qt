# TODO:
# - python support (PySide)
# - qt5
Summary:	Qt utility library for GEGL
Summary(pl.UTF-8):	Biblioteka narzędziowa Qt dla biblioteki GEGL
Name:		gegl-qt
Version:	0.0.7
Release:	1
License:	LGPL v3+
Group:		Libraries
Source0:	ftp://ftp.gimp.org/pub/gegl-qt/0.0/%{name}-%{version}.tar.bz2
# Source0-md5:	fbb0692af354d404615980a68c8a88f4
# git diff 0.0.7 4f46898e7dfaade23553f167bb03caf95171c0e7 (before switch to gegl 0.3)
# (then adjusted to apply on dist tarball)
Patch0:		%{name}-git.patch
URL:		http://www.gegl.org/
BuildRequires:	doxygen
BuildRequires:	gegl-devel >= 0.2.0
BuildRequires:	pkgconfig
BuildRequires:	qt4-qmake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Qt utility library for GEGL.

%description -l pl.UTF-8
Biblioteka narzędziowa Qt dla biblioteki GEGL.

%package -n gegl-qt4
Summary:	Qt 4 utility library for GEGL
Summary(pl.UTF-8):	Biblioteka narzędziowa Qt dla biblioteki GEGL
Group:		X11/Libraries
Requires:	gegl >= 0.2.0

%description -n gegl-qt4
Qt 4 utility library for GEGL.

%description -n gegl-qt4 -l pl.UTF-8
Biblioteka narzędziowa Qt 4 dla biblioteki GEGL.

%package -n gegl-qt4-devel
Summary:	Header files for gegl-qt4 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki gegl-qt4
Group:		Development/Libraries
Requires:	gegl-qt4 = %{version}-%{release}
Requires:	gegl-devel >= 0.2.0

%description -n gegl-qt4-devel
Header files for gegl-qt4 library.

%description -n gegl-qt4-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki gegl-qt4.

%package apidocs
Summary:	gegl library API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki gegl
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
gegl library API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki gegl.

%prep
%setup -q
%patch0 -p1

%build
qmake-qt4 \
	QMAKE_CXX="%{__cxx}" \
	QMAKE_CXXFLAGS_RELEASE="%{rpmcxxflags}" \
	QMAKE_LFLAGS_RELEASE="%{rpmldflags}"

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -n gegl-qt4
%defattr(644,root,root,755)
%doc README.txt
%attr(755,root,root) %{_libdir}/libgegl-qt4-0.1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgegl-qt4-0.1.so.0
%attr(755,root,root) %{_libdir}/gegl-0.2/libgegl-qt4-display.so
%dir %{_libdir}/qt4/imports/GeglQt4
%attr(755,root,root) %{_libdir}/qt4/imports/GeglQt4/libgegl-qt4-0.1.so
%{_libdir}/qt4/imports/GeglQt4/qmldir

%files -n gegl-qt4-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgegl-qt4-0.1.so
%{_includedir}/gegl-qt4-0.1
%{_pkgconfigdir}/gegl-qt4-0.1.pc

%files apidocs
%defattr(644,root,root,755)
%doc doc/html/*
