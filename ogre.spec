%define	oname		OGRE
%define	name		ogre
%define	version		1.4.0
%define rel		1
%define	release		%mkrel %rel

%define	major		14
%define	lib_name_orig	lib%{name}
%define	lib_name	%mklibname %{name} %{major}
%define	lib_name_devel	%mklibname %{name} %{major} -d
%{expand:%%define filever %(echo v%{version}| tr . -)}

Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}-linux_osx-%{filever}.tar.bz2
License:	LGPL
Group:		System/Libraries
URL:		http://www.ogre3d.org/
Summary:	Object-Oriented Graphics Rendering Engine
BuildRequires:	zlib-devel devil-devel >= 1.6.6-3mdk X11-devel MesaGLU-devel
BuildRequires:	jpeg-devel mng-devel tiff-devel SDL-devel lcms-devel nas-devel
BuildRequires:	gtkmm2.4-devel libglademm2.4-devel zziplib-devel
BuildRequires:	OpenEXR-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
OGRE  (Object-Oriented  Graphics  Rendering  Engine)  is a scene-oriented,
flexible 3D engine written in C++ designed to make it easier  and  more
intuitive for developers to produce games and demos utilising 3D hardware.
The class library abstracts all the details  of  using the underlying system
libraries like Direct3D and OpenGL and provides an interface based on world
objects and other intuitive classes.

%package -n	%{lib_name}
Summary:	Libraries needed for programs using %{oname}
Group:		System/Libraries
Provides:	%{lib_name_orig}
Provides:	%{name}
Obsoletes:	%mklibname ogre 5

%description -n	%{lib_name}
OGRE  (Object-Oriented  Graphics  Rendering  Engine)  is a scene-oriented,
flexible 3D engine written in C++ designed to make it easier  and  more
intuitive for developers to produce games and demos utilising 3D hardware.
The class library abstracts all the details  of  using the underlying system
libraries like Direct3D and OpenGL and provides an interface based on world
objects and other intuitive classes.

%package -n	%{lib_name_devel}
Summary:	Development headers and libraries for writing programs using %{oname}
Group:		Development/C++
Requires:	%{lib_name} = %{version}
Provides:	%{lib_name_orig}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%mklibname -d ogre 5

%description -n	%{lib_name_devel}
Development headers and libraries for writing programs using %{oname}

%prep
%setup -q -n %{name}new
find -type d -name CVS|xargs rm -rf

%build
%configure2_5x	--with-pic \
		--with-cfgtk=gtk \
		--disable-cg \
		--enable-openexr
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%post -n %{lib_name} -p /sbin/ldconfig
%postun -n %{lib_name} -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files -n %{lib_name}
%defattr(644,root,root,755)
%doc AUTHORS BUGS LINUX.DEV
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/*.so.%{major}*
%{_libdir}/%{oname}
%{_datadir}/%{oname}

%files -n %{lib_name_devel}
%defattr(644,root,root,755)
%doc Docs/*
%defattr(-,root,root)
%{_libdir}/lib*.so
%{_libdir}/*.la
%{_libdir}/pkgconfig/%{oname}.pc
%{_includedir}/%{oname}


