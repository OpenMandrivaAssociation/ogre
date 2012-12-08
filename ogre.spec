%define	oname OGRE
################################################################################
# !!! Never backport this package as it requires full rebuild of all based games
%define	version 1.8.0
################################################################################
%define	uversion %(echo %{version}| tr . _)
%define	libname %mklibname %{name} %{uversion}
%define	devname %mklibname %{name} -d
%define	filever %(echo v%{version}| tr . -)

Summary:	Object-Oriented Graphics Rendering Engine
Name:		ogre
Version:	%{version}
Release:	1
License:	LGPLv2+
Group:		System/Libraries
URL:		http://www.ogre3d.org/
Source0:	http://downloads.sourceforge.net/ogre/%{name}_src_%{filever}.tar.bz2
Patch0:		ogre_src_v1-8-0-link.patch

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
%patch0 -p0

%build
%cmake -DOGRE_INSTALL_SAMPLES:BOOL=ON -DOGRE_INSTALL_SAMPLES_SOURCE:BOOL=ON
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


%changelog
* Wed Jun 13 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.8.0-1
+ Revision: 805465
- unpackaged files fix
- version update 1.8.0

* Fri Jun 08 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.7.4-2
+ Revision: 803652
- rebuild for boost libs
- cleaned up spec

* Mon Jan 23 2012 Andrey Bondrov <abondrov@mandriva.org> 1.7.4-1
+ Revision: 767076
- New version 1.7.4

* Thu Nov 24 2011 Andrey Bondrov <abondrov@mandriva.org> 1.7.3-2
+ Revision: 733134
- Enable cg support

* Wed Nov 16 2011 Andrey Bondrov <abondrov@mandriva.org> 1.7.3-1
+ Revision: 730842
- New version 1.7.3

* Tue Mar 15 2011 Funda Wang <fwang@mandriva.org> 1.7.2-2
+ Revision: 644919
- rebuild for new boost

* Sun Feb 06 2011 Funda Wang <fwang@mandriva.org> 1.7.2-1
+ Revision: 636416
- update file list
- install samples source also
- tighten BR
- update BR
- 1.7.2

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 1.6.5-4mdv2011.0
+ Revision: 613172
- the mass rebuild of 2010.1 packages

* Fri Feb 12 2010 Funda Wang <fwang@mandriva.org> 1.6.5-3mdv2010.1
+ Revision: 504767
- add req on CEGUI0.6

* Fri Feb 12 2010 Funda Wang <fwang@mandriva.org> 1.6.5-2mdv2010.1
+ Revision: 504741
- BR CEGUI0.6
- rebuild

* Thu Jan 28 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 1.6.5-1mdv2010.1
+ Revision: 497488
- update to new version 1.6.5

* Sat Aug 22 2009 Emmanuel Andry <eandry@mandriva.org> 1.6.3-1mdv2010.0
+ Revision: 419736
- New version 1.6.3
- rediff P1 and P4

* Sun Jul 26 2009 Emmanuel Andry <eandry@mandriva.org> 1.6.2-1mdv2010.0
+ Revision: 400324
- New version 1.6.2

* Wed Feb 11 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1.6.1-1mdv2009.1
+ Revision: 339557
- do not build with -Werror=format-string
- update to new version 1.6.1

* Fri Nov 14 2008 Oden Eriksson <oeriksson@mandriva.com> 1.6.0-3mdv2009.1
+ Revision: 303353
- package the rcapsdump binary as well
- fix P1
- openexr isn't suported anymore, nuke it
- rebuilt against new libxcb

  + Tomasz Pawel Gajc <tpg@mandriva.org>
    - update to new version 1.6.0

* Sat Oct 11 2008 Adam Williamson <awilliamson@mandriva.org> 1.4.9-5mdv2009.1
+ Revision: 291817
- rebuild for changed CEGUI major

* Tue Sep 02 2008 Emmanuel Andry <eandry@mandriva.org> 1.4.9-4mdv2009.0
+ Revision: 278765
- remove bundled tinyxml ang glew headers
- remove header from tree to ensure they won't be used

* Mon Sep 01 2008 Emmanuel Andry <eandry@mandriva.org> 1.4.9-3mdv2009.0
+ Revision: 278061
- set define _disable_ld_no_undefined to 0, build fine on klodia (so, if this cannot build on cluster, we should look for a missing BR issue)

* Tue Aug 26 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.4.9-2mdv2009.0
+ Revision: 276055
- define _disable_ld_no_undefined because there are lot of unverlinking issues against CEGUI library, anyone who have time please feel free to provide a real fix :)

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild early 2009.0 package (before pixel changes)

  + Funda Wang <fwang@mandriva.org>
    - BR libtool
    - fix configure parameters
    - add debian patches
    - New version 1.4.9

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Mon May 12 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.4.8-1mdv2009.0
+ Revision: 206375
- new version

* Thu Apr 24 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.4.7-1mdv2009.0
+ Revision: 197244
- new version
- fix libification
- move samples into their own subpackage
- do not package useless docs
- Patch0: nuke rpath
- Patch1: use system wide glew library
- install missing headers
- fix patch in configuration files
- add lot of missing buildrequires

* Thu Feb 21 2008 Emmanuel Andry <eandry@mandriva.org> 1.4.6-1mdv2008.1
+ Revision: 173579
- New version

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Dec 15 2007 Emmanuel Andry <eandry@mandriva.org> 1.4.5-1mdv2008.1
+ Revision: 120421
- New version

* Thu Sep 06 2007 Adam Williamson <awilliamson@mandriva.org> 1.4.4-1mdv2008.0
+ Revision: 80598
- move plugins out of lib package to main package
- use Fedora license policy
- new devel policy
- new release 1.4.4

* Thu May 24 2007 Adam Williamson <awilliamson@mandriva.org> 1.4.1-1mdv2008.0
+ Revision: 30874
- package example code, fix paths in Samples/Common/bin/plugins.cfg (Peter Chapman bug #30997)
- 1.4.1

* Sat Apr 28 2007 Olivier Blin <blino@mandriva.org> 1.4.0-1mdv2008.0
+ Revision: 19022
- obsolete old library packages (major 13)
- conflict with old libogre packages previously containing binaries
- move binaries and doc in a new ogre package
- do not make the library provide ogre and libogre anymore
- move LINUX.DEV doc in devel package
- use makeinstall macro to fix samples installation
- remove data dir (not installed anymore)
- use 1_4_0 as package library version since upstream does not specify version anymore in the library (the API being changed every release)
- buildrequire freeimage-devel instead of other image libraries
- do not use SDL platform, it does not exist anymore
- 1.4.0

