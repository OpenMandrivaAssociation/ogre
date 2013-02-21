%define	oname OGRE
################################################################################
# !!! Never backport this package as it requires full rebuild of all based games
%define	version 1.8.1
################################################################################
%define	uversion %(echo %{version}| tr . _)
%define	libname %mklibname %{name} %{uversion}
%define	devname %mklibname %{name} -d
%define	filever %(echo v%{version}| tr . -)

Summary:	Object-Oriented Graphics Rendering Engine
Name:		ogre
Version:	%{version}
Release:	2
License:	LGPLv2+
Group:		System/Libraries
URL:		http://www.ogre3d.org/
Source0:	http://downloads.sourceforge.net/ogre/%{name}_src_%{filever}.tar.bz2
Source100:	%{name}.rpmlintrc

BuildRequires:	cmake
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xaw7)
BuildRequires:	pkgconfig(xrandr)
BuildRequires:	pkgconfig(xt)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(OIS)
BuildRequires:	boost-devel
BuildRequires:	freeimage-devel
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(zziplib)
BuildRequires:	pkgconfig(cppunit)
#Requires to build cg-plugin, but we cannot do it as cg-devel is in Non-Free
#BuildRequires:	cg-devel
#Be sure to build OGRE without cg-devel
BuildConflicts:	cg-devel
Conflicts:	libogre < 1.4.9
Suggests:	ogre-cg-plugin = %{version}

%description
OGRE  (Object-Oriented  Graphics  Rendering  Engine)  is a scene-oriented,
flexible 3D engine written in C++ designed to make it easier  and  more
intuitive for developers to produce games and demos utilising 3D hardware.
The class library abstracts all the details  of  using the underlying system
libraries like Direct3D and OpenGL and provides an interface based on world
objects and other intuitive classes.

%package -n %{libname}
Summary:	Libraries needed for programs using %{oname}
Group:		System/Libraries

%description -n %{libname}
OGRE  (Object-Oriented  Graphics  Rendering  Engine)  is a scene-oriented,
flexible 3D engine written in C++ designed to make it easier  and  more
intuitive for developers to produce games and demos utilising 3D hardware.
The class library abstracts all the details  of  using the underlying system
libraries like Direct3D and OpenGL and provides an interface based on world
objects and other intuitive classes.

%package -n %{devname}
Summary:	Development headers and libraries for writing programs using %{oname}
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{devname}
Development headers and libraries for writing programs using %{oname}

%package samples
Summary:	Samples for %{oname}
Group:		System/Libraries

%description samples
Samples for %{oname}.

%prep
%setup -qn %{name}_src_%{filever}

%build
%cmake \
	-DOGRE_INSTALL_SAMPLES:BOOL=ON \
	-DOGRE_INSTALL_SAMPLES_SOURCE:BOOL=ON
%make

%install
%makeinstall_std -C build

%files
%doc AUTHORS BUGS
%{_bindir}/OgreMeshUpgrader
%{_bindir}/OgreXMLConverter
%dir %{_libdir}/%{oname}
%{_libdir}/%{oname}/*.so*
%dir %{_datadir}/%{oname}

%files -n %{libname}
%{_libdir}/*.so.%{version}

%files -n %{devname}
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/%{oname}/cmake
%{_includedir}/%{oname}

%files samples
%{_bindir}/SampleBrowser
%{_datadir}/%{oname}/*.cfg
%{_datadir}/%{oname}/CMakeLists.txt
%{_datadir}/%{oname}/media
%{_datadir}/%{oname}/Samples
%{_libdir}/%{oname}/Samples


