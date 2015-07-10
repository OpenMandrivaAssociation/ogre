%define	oname OGRE
################################################################################
# !!! Never backport this package as it requires full rebuild of all based games
################################################################################
%define	uversion %(echo %{version})
%define	libmain %mklibname OgreMain %{uversion}
%define	libpag %mklibname OgrePaging %{uversion}
%define	libprop %mklibname OgreProperty %{uversion}
%define	librtss %mklibname OgreRTShaderSystem %{uversion}
%define	libterr %mklibname OgreTerrain %{uversion}
%define	libolay %mklibname OgreOverlay %{uversion}
%define	libvolm %mklibname OgreVolume %{uversion}
%define	devname %mklibname %{name} -d
%define	filever %(echo v%{version}| tr . -)
%define Werror_cflags %nil


Summary:	Object-Oriented Graphics Rendering Engine
Name:		ogre
Version:	1.9.0
Release:	6
License:	LGPLv2+
Group:		System/Libraries
Url:		http://www.ogre3d.org/
Source0:	http://downloads.sourceforge.net/ogre/%{name}-%{version}-clean.tar.bz2
Patch0:         ogre-1.7.2-rpath.patch
Patch1:         ogre-1.9.0-glew.patch
Patch3:         ogre-1.7.2-fix-ppc-build.patch
Patch5:         ogre-1.9.0-build-rcapsdump.patch
Patch6:         ogre-thread.patch
Patch7:         ogre-1.9.0-dynlib-allow-no-so.patch
Patch8:         ogre-1.9.0-cmake-freetype.patch
Patch9:         ogre-1.9.0-cmake_build-fix.patch
Patch10:        ogre-aarch64.patch

Source100:	%{name}.rpmlintrc

BuildRequires:	cmake
BuildRequires:	boost-devel
BuildRequires:	freeimage-devel
BuildRequires:	pkgconfig(cppunit)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(OIS)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xaw7)
BuildRequires:	pkgconfig(xrandr)
BuildRequires:	pkgconfig(xt)
BuildRequires:	pkgconfig(zziplib)
BuildRequires:	tinyxml-devel
BuildRequires:	doxygen

#Requires to build cg-plugin, but we cannot do it as cg-devel is in Non-Free
#BuildRequires:	cg-devel
#Be sure to build OGRE without cg-devel
BuildConflicts:	cg-devel
Conflicts:	libogre < 1.4.9
Suggests:	ogre-cg-plugin = %{EVRD}

%description
OGRE  (Object-Oriented  Graphics  Rendering  Engine)  is a scene-oriented,
flexible 3D engine written in C++ designed to make it easier  and  more
intuitive for developers to produce games and demos utilising 3D hardware.
The class library abstracts all the details  of  using the underlying system
libraries like Direct3D and OpenGL and provides an interface based on world
objects and other intuitive classes.

%package -n %{libmain}
Summary:	Libraries needed for programs using %{oname}
Group:		System/Libraries
Obsoletes:	%{_lib}ogre1_8_1 < 1.8.1-2

%description -n %{libmain}
This package contains a shared library for %{name}.

%package -n %{libpag}
Summary:	Libraries needed for programs using %{oname}
Group:		System/Libraries
Conflicts:	%{_lib}ogre1_8_1 < 1.8.1-2

%description -n %{libpag}
This package contains a shared library for %{name}.

%package -n %{libprop}
Summary:	Libraries needed for programs using %{oname}
Group:		System/Libraries
Conflicts:	%{_lib}ogre1_8_1 < 1.8.1-2

%description -n %{libprop}
This package contains a shared library for %{name}.

%package -n %{librtss}
Summary:	Libraries needed for programs using %{oname}
Group:		System/Libraries
Conflicts:	%{_lib}ogre1_8_1 < 1.8.1-2

%description -n %{librtss}
This package contains a shared library for %{name}.

%package -n %{libterr}
Summary:	Libraries needed for programs using %{oname}
Group:		System/Libraries
Conflicts:	%{_lib}ogre1_8_1 < 1.8.1-2

%description -n %{libterr}
This package contains a shared library for %{name}.

%package -n %{libolay}
Summary:	Libraries needed for programs using %{oname}
Group:		System/Libraries
Conflicts:	%{_lib}ogre1_8_1 < 1.8.1-2

%description -n %{libolay}
This package contains a shared library for %{name}.

%package -n %{libvolm}
Summary:	Libraries needed for programs using %{oname}
Group:		System/Libraries
Conflicts:	%{_lib}ogre1_8_1 < 1.8.1-2

%description -n %{libvolm}
This package contains a shared library for %{name}.

%package -n %{devname}
Summary:	Development headers and libraries for writing programs using %{oname}
Group:		Development/C++
Requires:	%{libmain} = %{EVRD}
Requires:	%{libpag} = %{EVRD}
Requires:	%{libprop} = %{EVRD}
Requires:	%{librtss} = %{EVRD}
Requires:	%{libterr} = %{EVRD}
Requires:	%{libolay} = %{EVRD}
Requires:	%{libvolm} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n	%{devname}
Development headers and libraries for writing programs using %{oname}

%package samples
Summary:	Samples for %{oname}
Group:		System/Libraries

%description samples
Samples for %{oname}.

%package	docs
Summary:	Samples for %{oname}
Group:		Documentation

%description docs
Docs for %{oname}.

%prep
%setup -qn %{name}-%{version}
%apply_patches

find . -type f -name "*.h"-o -name "*.cpp" -exec chmod 644 {} \;

%build
#https://ogre3d.atlassian.net/browse/OGRE-332
%ifarch %{ix86}
export CXXFLAGS="%{optflags} -msse -Wstrict-aliasing=0 -Wno-error"
%endif

%cmake \
	-DOGRE_INSTALL_SAMPLES:BOOL=ON \
	-DOGRE_BUILD_RTSHADERSYSTEM_EXT_SHADERS=1 \
	-DOGRE_INSTALL_SAMPLES_SOURCE:BOOL=ON
%make

%install
%makeinstall_std -C build

rm -f %{buildroot}%{_datadir}/OGRE/docs/CMakeLists.txt
find %{buildroot} -size 0 -delete


%files
%doc AUTHORS BUGS
%{_bindir}/OgreMeshUpgrader
%{_bindir}/OgreXMLConverter
%{_bindir}/rcapsdump
%dir %{_libdir}/%{oname}
%{_libdir}/%{oname}/*.so.%{version}*
%{_libdir}/%{oname}/*.so
%dir %{_datadir}/%{oname}

%files -n %{libmain}
%doc AUTHORS BUGS
%{_libdir}/libOgreMain.so.%{version}

%files -n %{libpag}
%doc AUTHORS BUGS
%{_libdir}/libOgrePaging.so.%{version}

%files -n %{libprop}
%doc AUTHORS BUGS
%{_libdir}/libOgreProperty.so.%{version}

%files -n %{librtss}
%{_libdir}/libOgreRTShaderSystem.so.%{version}

%files -n %{libterr}
%doc AUTHORS BUGS
%{_libdir}/libOgreTerrain.so.%{version}

%files -n %{libolay}
%doc AUTHORS BUGS
%{_libdir}/libOgreOverlay.so.%{version}

%files -n %{libvolm}
%doc AUTHORS BUGS
%{_libdir}/libOgreVolume.so.%{version}

%files -n %{devname}
%doc AUTHORS BUGS
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/%{oname}/cmake
%{_includedir}/%{oname}

%files samples
%doc AUTHORS BUGS
%{_bindir}/SampleBrowser
%{_datadir}/%{oname}/*.cfg
%{_datadir}/%{oname}/CMakeLists.txt
%{_datadir}/%{oname}/Media
%{_datadir}/%{oname}/Samples
%{_libdir}/%{oname}/Samples

%files docs
%doc AUTHORS BUGS
%{_datadir}/%{oname}/docs

