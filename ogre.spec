%define	oname OGRE
%define version 1.7.2
%define uversion %(echo %{version}| tr . _)
%define libname %mklibname %{name} %{uversion}
%define	develname %mklibname %{name} -d
%define filever %(echo v%{version}| tr . -)

Summary:	Object-Oriented Graphics Rendering Engine
Name:		ogre
Version:	%{version}
Release:	%mkrel 1
License:	LGPLv2+
Group:		System/Libraries
URL:		http://www.ogre3d.org/
Source0:	http://downloads.sourceforge.net/ogre/%{name}_src_%{filever}.tar.bz2
BuildRequires:	libx11-devel
BuildRequires:	libxaw-devel
BuildRequires:	libxrandr-devel
BuildRequires:	libxt-devel
BuildRequires:	mesagl-devel
BuildRequires:	mesaglu-devel
BuildRequires:	ois-devel
BuildRequires:	boost-devel
BuildRequires:	freeimage-devel
BuildRequires:	freetype2-devel
BuildRequires:	zziplib-devel
BuildRequires:	cppunit-devel
BuildRequires:	cmake
Conflicts:	libogre < 1.4.9
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
Obsoletes:	%mklibname ogre 13

%description -n %{libname}
OGRE  (Object-Oriented  Graphics  Rendering  Engine)  is a scene-oriented,
flexible 3D engine written in C++ designed to make it easier  and  more
intuitive for developers to produce games and demos utilising 3D hardware.
The class library abstracts all the details  of  using the underlying system
libraries like Direct3D and OpenGL and provides an interface based on world
objects and other intuitive classes.

%package -n %{develname}
Summary:	Development headers and libraries for writing programs using %{oname}
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%mklibname -d %{name} 13
Obsoletes:	%mklibname %{name} 1_4_1 -d

%description -n	%{develname}
Development headers and libraries for writing programs using %{oname}

%package samples
Summary:	Samples for %{oname}
Group:		System/Libraries

%description samples
Samples for %{oname}.

%prep
%setup -qn %{name}_src_%{filever}

%build
%cmake -DOGRE_INSTALL_SAMPLES:BOOL=ON
%make

%install
rm -rf %{buildroot}
%makeinstall_std -C build

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS BUGS
%defattr(-,root,root)
%{_bindir}/OgreMeshUpgrader
%{_bindir}/OgreXMLConverter
%dir %{_libdir}/%{oname}
%{_libdir}/%{oname}/*.so
%dir %{_datadir}/%{oname}

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{version}

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/%{oname}/cmake
%{_includedir}/%{oname}

%files samples
%defattr(-,root,root)
%{_bindir}/SampleBrowser
%{_datadir}/%{oname}/media
%{_datadir}/%{oname}/Samples
%{_libdir}/%{oname}/Samples
