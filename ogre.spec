%define	oname		OGRE
%define	name		ogre
%define	version		1.4.5
%define rel		1
%define	release		%mkrel %rel

%define uversion %(echo %{version}| tr . _)
%define	lib_name_orig	lib%{name}
%define	lib_name	%mklibname %{name} %{uversion}
%define	lib_name_devel	%mklibname %{name} -d
%{expand:%%define filever %(echo v%{version}| tr . -)}

Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}-linux_osx-%{filever}.tar.bz2
License:	LGPLv2+
Group:		System/Libraries
URL:		http://www.ogre3d.org/
Summary:	Object-Oriented Graphics Rendering Engine
BuildRequires:	X11-devel MesaGLU-devel	SDL-devel
BuildRequires:	freeimage-devel lcms-devel nas-devel
BuildRequires:	gtkmm2.4-devel libglademm2.4-devel zziplib-devel
BuildRequires:	OpenEXR-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Conflicts:	libogre

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
Obsoletes:	%mklibname ogre 13

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
Obsoletes:	%mklibname -d %{name} 13
Obsoletes:	%mklibname %{name} 1_4_1 -d

%description -n	%{lib_name_devel}
Development headers and libraries for writing programs using %{oname}

%prep
%setup -q -n %{name}new
find -type d -name CVS|xargs rm -rf

# Correct path to lib dir (suggested by Peter Chapman)
perl -pi -e 's,/usr/local/lib,%_libdir,g' Samples/Common/bin/plugins.cfg
# Don't include this plugin as it's not built (Peter Chapman)
perl -pi -e 's,Plugin=Plugin_CgProgramManager.so,,g' Samples/Common/bin/plugins.cfg

%build
%configure2_5x	--with-pic \
		--with-cfgtk=gtk \
		--disable-cg \
		--enable-openexr
%make

%install
rm -rf %{buildroot}
%makeinstall

%post -n %{lib_name} -p /sbin/ldconfig
%postun -n %{lib_name} -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/%{oname}

%files -n %{lib_name}
%defattr(-,root,root)
%{_libdir}/libOgreMain-%{version}.so
%{_libdir}/libCEGUIOgreRenderer-%{version}.so

%files -n %{lib_name_devel}
%defattr(644,root,root,755)
%doc Docs/* LINUX.DEV Samples
%defattr(-,root,root)
%{_libdir}/libOgreMain.so
%{_libdir}/libCEGUIOgreRenderer.so
%{_libdir}/libOgreMain.la
%{_libdir}/libCEGUIOgreRenderer.la
%{_libdir}/pkgconfig/%{oname}.pc
%{_libdir}/pkgconfig/CEGUI-%{oname}.pc

%{_includedir}/%{oname}

