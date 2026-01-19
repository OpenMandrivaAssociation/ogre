%define	oname OGRE
################################################################################
# !!! Never backport this package as it requires full rebuild of all based games
################################################################################
%define	libmain %mklibname OgreMain
%define	libpag %mklibname OgrePaging
%define	libprop %mklibname OgreProperty
%define	librtss %mklibname OgreRTShaderSystem
%define	libterr %mklibname OgreTerrain
%define	libolay %mklibname OgreOverlay
%define	libvolm %mklibname OgreVolume
%define	libbites %mklibname OgreBites
%define	libmeshload %mklibname MeshLodGenerator
%define	oldlibmain %mklibname OgreMain %{version}
%define	oldlibpag %mklibname OgrePaging %{version}
%define	oldlibprop %mklibname OgreProperty %{version}
%define	oldlibrtss %mklibname OgreRTShaderSystem %{version}
%define	oldlibterr %mklibname OgreTerrain %{version}
%define	oldlibolay %mklibname OgreOverlay %{version}
%define	oldlibvolm %mklibname OgreVolume %{version}
%define	oldlibbites %mklibname OgreBites %{version}
%define	oldlibmeshload %mklibname MeshLodGenerator %{version}
%define	devname %mklibname %{name} -d
%define	filever %(echo v%{version}| tr . -)
%global optflags %{optflags} -I%{_includedir}/SDL2 -fno-strict-aliasing
#define _disable_lto 1

%define major %(echo %{version} |cut -d. -f1-2)

# Make sure the version here is in sync with
# Components/Overlay/CMakeLists.txt
%define	imgui_ver 1.91.9b
%define imgui_short_ver %(echo %imgui_ver | cut -d. -f1-2)

Summary:	Object-Oriented Graphics Rendering Engine
Name:		ogre
Version:	14.5.1
Release:	1
License:	LGPLv2+
Group:		System/Libraries
Url:		https://www.ogre3d.org/
Source0:	https://github.com/OGRECave/ogre/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/ocornut/imgui/archive/%{imgui_short_ver}/imgui-%{imgui_ver}.tar.gz

Patch1:		ogre-1.12.9-compile.patch
Patch2:		ogre-13.2.4-linkage.patch
#Patch6:         ogre-thread.patch
# Patch from Solus. Force OpenEXR 3 instead 2.
Patch7:		OpenEXR-instead-of-ilmbase.patch

Source100:	%{name}.rpmlintrc

BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	boost-devel
BuildRequires:	freeimage-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  swig
BuildRequires:	pkgconfig(cppunit)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(egl)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
# Disable, until mono is not instalable in Cooker
#BuildRequires:  pkgconfig(mono)
BuildRequires:	pkgconfig(OIS)
# Ogre still depend on OpenEXR v2. Let's try patch it for v3.
BuildRequires:  pkgconfig(OpenEXR)
BuildRequires:  pkgconfig(python)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xrandr)
BuildRequires:	pkgconfig(xt)
BuildRequires:	pkgconfig(zziplib)
BuildRequires:	tinyxml-devel
BuildRequires:  pugixml-devel
BuildRequires:	doxygen

#Requires to build cg-plugin, but we cannot do it as cg-devel is in Non-Free
#BuildRequires:	cg-devel
#Be sure to build OGRE without cg-devel
BuildConflicts:	cg-devel
Conflicts:	libogre < 1.4.9
Suggests:	ogre-cg-plugin = %{EVRD}
# This used to be in the main ogre package, let's make sure
# we don't get nasty surprises
Suggests:	python-ogre = %{EVRD}

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
%rename %{oldlibmain}

%description -n %{libmain}
This package contains a shared library for %{name}.

%package -n %{libpag}
Summary:	Libraries needed for programs using %{oname}
Group:		System/Libraries
Conflicts:	%{_lib}ogre1_8_1 < 1.8.1-2
%rename %{oldlibpag}

%description -n %{libpag}
This package contains a shared library for %{name}.

%package -n %{libprop}
Summary:	Libraries needed for programs using %{oname}
Group:		System/Libraries
Conflicts:	%{_lib}ogre1_8_1 < 1.8.1-2
%rename %{oldlibprop}

%description -n %{libprop}
This package contains a shared library for %{name}.

%package -n %{librtss}
Summary:	Libraries needed for programs using %{oname}
Group:		System/Libraries
Conflicts:	%{_lib}ogre1_8_1 < 1.8.1-2
%rename %{oldlibrtss}

%description -n %{librtss}
This package contains a shared library for %{name}.

%package -n %{libterr}
Summary:	Libraries needed for programs using %{oname}
Group:		System/Libraries
Conflicts:	%{_lib}ogre1_8_1 < 1.8.1-2
%rename %{oldlibterr}

%description -n %{libterr}
This package contains a shared library for %{name}.

%package -n %{libolay}
Summary:	Libraries needed for programs using %{oname}
Group:		System/Libraries
Conflicts:	%{_lib}ogre1_8_1 < 1.8.1-2
%rename %{oldlibolay}

%description -n %{libolay}
This package contains a shared library for %{name}.

%package -n %{libvolm}
Summary:	Libraries needed for programs using %{oname}
Group:		System/Libraries
Conflicts:	%{_lib}ogre1_8_1 < 1.8.1-2
%rename %{oldlibvolm}

%description -n %{libvolm}
This package contains a shared library for %{name}.

%package -n %{libbites}
Summary:	Libraries needed for programs using %{oname}
Group:		System/Libraries
Conflicts:	%{_lib}ogre1_8_1 < 1.8.1-2
%rename %{oldlibbites}

%description -n %{libbites}
This package contains a shared library for %{name}.

%package -n %{libmeshload}
Summary:	Libraries needed for programs using %{oname}
Group:		System/Libraries
Conflicts:	%{_lib}ogre1_8_1 < 1.8.1-2
%rename %{oldlibmeshload}

%description -n %{libmeshload}
This package contains a shared library for %{name}.

%package -n python-ogre
Summary:	Python support for the Ogre 3D engine
Group:		System/Libraries

%description -n python-ogre
Python support for the Ogre 3D engine

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
Requires:	%{libbites} = %{EVRD}
Requires:	%{libmeshload} = %{EVRD}
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
%autosetup -p1 -a1
mkdir build
mv imgui-%{imgui_ver} build/imgui-%{imgui_ver}

find . -type f -name "*.h"-o -name "*.cpp" -exec chmod 644 {} \;

#https://ogre3d.atlassian.net/browse/OGRE-332
%ifarch %{ix86}
export CXXFLAGS="%{optflags} -msse -Wno-error -std=c++14"
%endif

# Don't install python bits to Debian specific directories
sed -i -e 's,lib/python${PYTHON_VERSION_MAJOR}.${PYTHON_VERSION_MINOR}/dist-packages/,%{python_sitelib}/,g' Components/Python/CMakeLists.txt

# As of Clang 15.0.5 and Ogre 13.5.3 LLVM crashes at compile time. As workaround use GCC for now.
export CC=gcc
export CXX=g++
# Deprecated bits like OGRE_NODELESS_POSITIONING are enabled because some
# packages (stuntrally etc.) still use those APIs.
# FIXME enable Java and C# once they're fixed to work with swig 4.x
%cmake \
        -DOGRE_BUILD_DOCS:BOOL=OFF \
        -DOGRE_BUILD_DEPENDENCIES=FALSE \
        -DOGRE_BUILD_PLUGIN_CG:BOOL=OFF \
        -DOGRE_INSTALL_SAMPLES:BOOL=ON \
        -DOGRE_INSTALL_SAMPLES_SOURCE:BOOL=ON \
        -DOGRE_CONFIG_MEMTRACK_RELEASE:BOOL=OFF \
	-DOGRE_BUILD_COMPONENT_OVERLAY:BOOL=ON \
	-DOGRE_BUILD_COMPONENT_OVERLAY_IMGUI:BOOL=ON \
	-DOGRE_BUILD_COMPONENT_CSHARP:BOOL=OFF \
	-DOGRE_BUILD_COMPONENT_JAVA:BOOL=OFF \
	-DOGRE_NODELESS_POSITIONING:BOOL=ON \
	-DOGRE_RESOURCEMANAGER_STRICT=0 \
	-G Ninja

%build
export CC=gcc
export CXX=g++
%ninja_build -C build

%install
%ninja_install -C build

rm -f %{buildroot}%{_datadir}/OGRE/docs/CMakeLists.txt
find %{buildroot} -size 0 -delete


%files
%doc AUTHORS
%{_bindir}/OgreMeshUpgrader
%{_bindir}/OgreXMLConverter
%{_bindir}/VRMLConverter
%dir %{_libdir}/%{oname}
%{_libdir}/%{oname}/*.so.%{major}*
%{_libdir}/%{oname}/*.so
%{_libdir}/libOgreBitesQt.so.%{major}
#dir %{_datadir}/%{oname}

%files -n python-ogre
%{python_sitelib}/Ogre

%files -n %{libmain}
%doc AUTHORS
%{_libdir}/libOgreMain.so.%{major}

%files -n %{libpag}
%doc AUTHORS
%{_libdir}/libOgrePaging.so.%{major}

%files -n %{libprop}
%doc AUTHORS
%{_libdir}/libOgreProperty.so.%{major}

%files -n %{librtss}
%{_libdir}/libOgreRTShaderSystem.so.%{major}

%files -n %{libterr}
%doc AUTHORS
%{_libdir}/libOgreTerrain.so.%{major}

%files -n %{libolay}
%doc AUTHORS
%{_libdir}/libOgreOverlay.so.%{major}

%files -n %{libvolm}
%doc AUTHORS
%{_libdir}/libOgreVolume.so.%{major}

%files -n %{libbites}
%doc AUTHORS
%{_libdir}/libOgreBites.so.%{major}

%files -n %{libmeshload}
%doc AUTHORS
%{_libdir}/libOgreMeshLodGenerator.so.%{major}

%files -n %{devname}
%doc AUTHORS
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/%{oname}/cmake
%{_includedir}/%{oname}

%files samples
%doc AUTHORS
%{_bindir}/SampleBrowser
%{_datadir}//OGRE-*.*/Media/
%{_libdir}/%{oname}/Samples
%{_datadir}/OGRE-*.*/*.cfg

%files docs
#doc AUTHORS
%{_docdir}/%{oname}/

