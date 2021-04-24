# TODO: qml plugin for qt5
#
# Conditional build:
%bcond_without	python	# Python (PySide) binding for Qt4 library
%bcond_without	qt4	# Qt4 library
%bcond_without	qt5	# Qt5 library
#
Summary:	Qt utility library for GEGL
Summary(pl.UTF-8):	Biblioteka narzędziowa Qt dla biblioteki GEGL
Name:		gegl-qt
Version:	0.0.7
Release:	1
License:	LGPL v3+
Group:		Libraries
Source0:	https://download.gimp.org/pub/gegl-qt/0.0/%{name}-%{version}.tar.bz2
# Source0-md5:	fbb0692af354d404615980a68c8a88f4
# git diff 0.0.7 4f46898e7dfaade23553f167bb03caf95171c0e7 (before switch to gegl 0.3)
# (then adjusted to apply on dist tarball)
Patch0:		%{name}-git.patch
Patch1:		%{name}-shiboken.patch
Patch2:		%{name}-qmake.patch
Patch3:		%{name}-qt5.patch
# https://gitlab.gnome.org/Archive/gegl-qt/-/commit/0e48db1e2baac9dde31b1a0b9add2ccd28df012b.patch (last commit)
Patch4:		%{name}-gegl-0.3.patch
Patch5:		%{name}-gegl-0.4.patch
Patch6:		%{name}-python-dirs.patch
URL:		https://www.gegl.org/
%if %{with qt4}
BuildRequires:	QtCore-devel >= 4
BuildRequires:	QtDeclarative-devel >= 4
BuildRequires:	QtGui-devel >= 4
%endif
%if %{with qt5}
BuildRequires:	Qt5Core-devel >= 5
BuildRequires:	Qt5Declarative-devel >= 5
BuildRequires:	Qt5Gui-devel >= 5
BuildRequires:	Qt5Widgets-devel >= 5
%endif
BuildRequires:	doxygen
BuildRequires:	gegl-devel >= 0.2.0
BuildRequires:	pkgconfig
%{?with_qt4:BuildRequires:	qt4-qmake >= 4}
%{?with_qt5:BuildRequires:	qt5-qmake >= 5}
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	texlive-format-pdflatex
BuildRequires:	texlive-latex-extend
%if %{with python}
BuildRequires:	python-PySide-devel >= 4.8_1.2.4-1
BuildRequires:	shiboken >= 1.2.4-3
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Qt utility library for GEGL.

%description -l pl.UTF-8
Biblioteka narzędziowa Qt dla biblioteki GEGL.

%package -n gegl-qt4
Summary:	Qt 4 utility library for GEGL
Summary(pl.UTF-8):	Biblioteka narzędziowa Qt 4 dla biblioteki GEGL
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
Requires:	QtCore-devel >= 4
Requires:	QtDeclarative-devel >= 4
Requires:	QtGui-devel >= 4
Requires:	gegl-qt4 = %{version}-%{release}
Requires:	gegl-devel >= 0.2.0

%description -n gegl-qt4-devel
Header files for gegl-qt4 library.

%description -n gegl-qt4-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki gegl-qt4.

%package -n python-gegl-qt4
Summary:	Python (PySide) binding for gegl-qt4 library
Summary(pl.UTF-8):	Wiązania Pythona (PySide) do biblioteki gegl-qt4
Group:		Libraries/Python
Requires:	gegl-qt4 = %{version}-%{release}
Requires:	python-PySide

%description -n python-gegl-qt4
Python (PySide) binding for gegl-qt4 library.

%description -n python-gegl-qt4 -l pl.UTF-8
Wiązania Pythona (PySide) do biblioteki gegl-qt4.

%package -n gegl-qt5
Summary:	Qt 5 utility library for GEGL
Summary(pl.UTF-8):	Biblioteka narzędziowa Qt 5 dla biblioteki GEGL
Group:		X11/Libraries
Requires:	gegl >= 0.2.0

%description -n gegl-qt5
Qt 5 utility library for GEGL.

%description -n gegl-qt5 -l pl.UTF-8
Biblioteka narzędziowa Qt 5 dla biblioteki GEGL.

%package -n gegl-qt5-devel
Summary:	Header files for gegl-qt5 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki gegl-qt5
Group:		Development/Libraries
Requires:	Qt5Core-devel >= 5
Requires:	Qt5Declarative-devel >= 5
Requires:	Qt5Gui-devel >= 5
Requires:	gegl-qt5 = %{version}-%{release}
Requires:	gegl-devel >= 0.2.0

%description -n gegl-qt5-devel
Header files for gegl-qt5 library.

%description -n gegl-qt5-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki gegl-qt5.

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
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
%if %{with qt4}
install -d build-qt4
cd build-qt4
qmake-qt4 ../gegl-qt.pro \
	QMAKE_CXX="%{__cxx}" \
	QMAKE_CXXFLAGS_RELEASE="%{rpmcxxflags}" \
	QMAKE_LFLAGS_RELEASE="%{rpmldflags}" \
	%{!?with_python:HAVE_PYSIDE=no}

%{__make}
cd ..
ln -snf build-qt4 build
%endif

%if %{with qt5}
install -d build-qt5
cd build-qt5
qmake-qt5 ../gegl-qt.pro \
	QMAKE_CXX="%{__cxx}" \
	QMAKE_CXXFLAGS_RELEASE="%{rpmcxxflags}" \
	QMAKE_LFLAGS_RELEASE="%{rpmldflags}"

%{__make}
cd ..
test -L build || ln -snf build-qt5 build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with qt4}
%{__make} -C build-qt4 install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

# extraneous symlink
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libgegl-qt4-0.1.so.0.0

%if %{with python}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean
%endif
%endif

%if %{with qt5}
%{__make} -C build-qt5 install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

# extraneous symlink
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libgegl-qt5-0.1.so.0.0
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%if %{with qt4}
%files -n gegl-qt4
%defattr(644,root,root,755)
%doc README.txt
%attr(755,root,root) %{_libdir}/libgegl-qt4-0.1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgegl-qt4-0.1.so.0
# not ready for gegl-0.4
#%attr(755,root,root) %{_libdir}/gegl-0.3/libgegl-qt4-display.so
%dir %{_libdir}/qt4/imports/GeglQt4
%attr(755,root,root) %{_libdir}/qt4/imports/GeglQt4/libgegl-qt4-0.1.so
%{_libdir}/qt4/imports/GeglQt4/qmldir

%files -n gegl-qt4-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgegl-qt4-0.1.so
%{_includedir}/gegl-qt4-0.1
%{_pkgconfigdir}/gegl-qt4-0.1.pc

%if %{with python}
%files -n python-gegl-qt4
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gegl-qt4-0.1/geglqt.so
%{py_sitedir}/pygeglqt4.py[co]
%endif
%endif

%if %{with qt5}
%files -n gegl-qt5
%defattr(644,root,root,755)
%doc README.txt
%attr(755,root,root) %{_libdir}/libgegl-qt5-0.1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgegl-qt5-0.1.so.0
# not ready for gegl-0.4
#%attr(755,root,root) %{_libdir}/gegl-0.3/libgegl-qt5-display.so
# not ready for qt5 plugin format (_disabled in qt5 patch)
#%dir %{_libdir}/qt4/imports/GeglQt4
#%attr(755,root,root) %{_libdir}/qt4/imports/GeglQt4/libgegl-qt4-0.1.so
#%{_libdir}/qt4/imports/GeglQt4/qmldir

%files -n gegl-qt5-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgegl-qt5-0.1.so
%{_includedir}/gegl-qt5-0.1
%{_pkgconfigdir}/gegl-qt5-0.1.pc
%endif

%files apidocs
%defattr(644,root,root,755)
%doc build/doc/html/*
