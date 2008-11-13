%define	oname OGRE
%define version 1.6.0
%define uversion %(echo %{version}| tr . _)
%define libname %mklibname %{name} %{uversion}
%define	develname %mklibname %{name} -d
%define filever %(echo v%{version}| tr . -)

Summary:	Object-Oriented Graphics Rendering Engine
Name:		ogre
Version:	%{version}
Release:	%mkrel 2
License:	LGPLv2+
Group:		System/Libraries
URL:		http://www.ogre3d.org/
Source0:	http://downloads.sourceforge.net/ogre/%{name}-%{filever}.tar.bz2
Patch0:		ogre-1.2.1-rpath.patch
Patch1:		ogre-1.4.6-system-glew.patch
Patch2:		ogre-1.4.9-as-needed.patch
Patch3:		ogre-1.4.9-cegui.patch
Patch4:		ogre-1.4.7-system-tinyxml.patch
BuildRequires:	X11-devel
BuildRequires:	MesaGLU-devel
BuildRequires:	SDL-devel
BuildRequires:	freeimage-devel
BuildRequires:	lcms-devel
BuildRequires:	nas-devel
BuildRequires:	gtkmm2.4-devel
BuildRequires:	libglademm2.4-devel
BuildRequires:	zziplib-devel
BuildRequires:	OpenEXR-devel
BuildRequires:	cppunit-devel
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	CEGUI-devel
BuildRequires:	ois-devel
BuildRequires:	glew-devel
BuildRequires:	libtool
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
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1
%patch2 -p0
%patch3 -p0
%patch4 -p1

find -type d -name CVS|xargs rm -rf

#be sure we won't use bundled glew
rm -rf RenderSystems/GL/include/GL/*
# remove included tinyxml headers to ensure use of system headers
rm Tools/XMLConverter/include/tiny*

# Correct path to lib dir (suggested by Peter Chapman)
perl -pi -e 's|/usr/local/lib|%{_libdir}|g' Samples/Common/bin/plugins.cfg
# Don't include this plugin as it's not built (Peter Chapman)
perl -pi -e 's|Plugin=Plugin_CgProgramManager.so||g' Samples/Common/bin/plugins.cfg
# (tpg) fix paths
sed -i -e 's|../../Media|%{_datadir}/%{name}/Samples|g' Samples/Common/bin/resources.cfg
sed -i -e 's|/usr/local|%{_libdir}|g' Samples/Common/bin/quake3settings.cfg

%build
%define _disable_ld_no_undefined 0

./bootstrap
%configure2_5x	\
	--with-pic \
	--with-gui=gtk \
	--disable-cg \
	--enable-openexr \
	--disable-devil

# Don't use rpath!
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
sed -i 's|-L%{_libdir}||g' `find -name Makefile`

%make

%install
rm -rf %{buildroot}
%makeinstall_std

# copy some forgotten headers ... (ogre4j needs them)
install -dm 755 %{buildroot}%{_includedir}/OGRE
install -m 644 OgreMain/include/OgreOptimisedUtil.h %{buildroot}%{_includedir}/OGRE
install -m 644 OgreMain/include/OgrePlatformInformation.h %{buildroot}%{_includedir}/OGRE

# (tpg) install samples
install -dm 755 %{buildroot}%{_datadir}/ogre/Samples
cp -R Samples/Media/* %{buildroot}%{_datadir}/ogre/Samples
install -m 644 Samples/Common/bin/*.cfg %{buildroot}%{_datadir}/ogre/Samples

# (tpg) move samples binaries to the right place
pushd %{buildroot}`pwd`/Samples/Common/bin
demo_list=`ls -1`
    for i in $demo_list; do
	install -m 755 $i %{buildroot}%{_bindir}/%{name}-$i
    done
popd

rm -rf %{buildroot}`pwd`/Samples/Common/bin

# (tpg) remove useless docs
rm -rf Docs/Samples
rm -rf Docs/src
rm -rf Docs/shadows/src

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
%{_bindir}/Ogre*
%{_libdir}/%{oname}/*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libOgreMain-%{version}.so
%{_libdir}/libCEGUIOgreRenderer-%{version}.so

%files -n %{develname}
%defattr(-,root,root)
%doc Docs/* LINUX.DEV
%defattr(-,root,root)
%{_libdir}/libOgreMain.so
%{_libdir}/libOgreMain.la
%{_libdir}/libCEGUIOgreRenderer.la
%{_libdir}/libCEGUIOgreRenderer.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/%{oname}

%files samples
%defattr(-,root,root)
%{_bindir}/%{name}-*
%{_datadir}/%{name}/Samples
