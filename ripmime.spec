%define	major 1
%define libname %mklibname ripmime %{major}
%define develname %mklibname ripmime -d

Summary:	Extracts attachments out of mailpack format emails
Name:		ripmime
Version:	1.4.0.10
Release:	3
License:	BSD
Group:		Networking/Mail
URL:		http://www.pldaniels.com/ripmime/
Source0:	http://www.pldaniels.com/ripmime/%{name}-%{version}.tar.gz
Patch0:		ripmime-shared.diff
Patch1:		ripmime-1.4.0.10-buffer_overflow.diff
BuildRequires:	autoconf automake libtool
BuildRequires:	ripole-devel

%description
ripMIME is a small program which has been developed as part of the
commercial Xamime development (http://www.xamime.com).

ripMIME has been written with one sole purpose in mind, to extract
the attached files out of a MIME encoded email package.

%package -n	%{libname}
Summary:	Shared %{name} library
Group:          System/Libraries

%description -n	%{libname}
ripMIME is a small program which has been developed as part of the
commercial Xamime development (http://www.xamime.com).

ripMIME has been written with one sole purpose in mind, to extract
the attached files out of a MIME encoded email package.

This package provides the shared %{name} library.

%package -n	%{develname}
Summary:	Development files for the %{name} library
Group:		Development/C
Provides:	%{name}-devel = %{version}
Provides:	lib%{name}-devel = %{version}
Requires:	%{libname} >= %{version}
Obsoletes:	%{mklibname ripmime 1 -d}

%description -n	%{develname}
ripMIME is a small program which has been developed as part of the
commercial Xamime development (http://www.xamime.com).

ripMIME has been written with one sole purpose in mind, to extract
the attached files out of a MIME encoded email package.

This package provides development files for the %{name} library.

%prep

%setup -q -n %{name}-%{version}
%patch0 -p0
%patch1 -p0

%build

%make \
    CFLAGS="%{optflags}" \
    libdir=%{_libdir} LDFLAGS="%{ldflags}"

%install
rm -rf %{buildroot}

%makeinstall_std \
    bindir=%{_bindir} \
    includedir=%{_includedir} \
    libdir=%{_libdir} \
    mandir=%{_mandir}

# cleanups
rm -f %{buildroot}%{_libdir}/*.*a

%files
%doc CHANGELOG CONTRIBUTORS INSTALL LICENSE README
%{_bindir}/*
%{_mandir}/man1/*

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%doc TODO
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%{_libdir}/*.so


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.4.0.10-2
+ Revision: 742486
- various fixes

* Tue Jun 28 2011 Oden Eriksson <oeriksson@mandriva.com> 1.4.0.10-1
+ Revision: 687887
- 1.4.0.10

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 1.4.0.9-3mdv2010.0
+ Revision: 442749
- rebuild

* Fri Dec 19 2008 Oden Eriksson <oeriksson@mandriva.com> 1.4.0.9-2mdv2009.1
+ Revision: 316155
- use LDFLAGS from the %%configure macro

* Fri Nov 07 2008 Oden Eriksson <oeriksson@mandriva.com> 1.4.0.9-1mdv2009.1
+ Revision: 300505
- 1.4.0.9

* Wed Nov 05 2008 Oden Eriksson <oeriksson@mandriva.com> 1.4.0.8-1mdv2009.1
+ Revision: 300061
- 1.4.0.8

* Mon Oct 13 2008 Oden Eriksson <oeriksson@mandriva.com> 1.4.0.7-4mdv2009.1
+ Revision: 293306
- added fixes from ripmime-1.4.dev (P1)

* Sun Jul 20 2008 Oden Eriksson <oeriksson@mandriva.com> 1.4.0.7-3mdv2009.0
+ Revision: 238998
- use -Wl,--as-needed -Wl,--no-undefined

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Sep 09 2007 Oden Eriksson <oeriksson@mandriva.com> 1.4.0.7-2mdv2008.0
+ Revision: 83495
- new devel name

* Tue Jul 10 2007 Oden Eriksson <oeriksson@mandriva.com> 1.4.0.7-1mdv2008.0
+ Revision: 51022
- 1.4.0.7
- rediffed the shared patch (P0)
- use the new %%serverbuild macro


* Thu Aug 10 2006 Oden Eriksson <oeriksson@mandriva.com> 1.4.0.7-0.dev.1mdv2007.0
- added P1 from the dev snap

* Wed Jan 18 2006 Oden Eriksson <oeriksson@mandriva.com> 1.4.0.6-4mdk
- make it install correctly on x86_64

* Sun Jan 08 2006 Oden Eriksson <oeriksson@mandriva.com> 1.4.0.6-3mdk
- make it compile on 10.0 too

* Sun Jan 08 2006 Oden Eriksson <oeriksson@mandriva.com> 1.4.0.6-2mdk
- use libtool

* Mon Dec 12 2005 Oden Eriksson <oeriksson@mandriva.com> 1.4.0.6-1mdk
- 1.4.0.6

* Sun Jun 12 2005 Oden Eriksson <oeriksson@mandriva.com> 1.4.0.5-1mdk
- 1.4.0.5

* Tue Mar 29 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 1.4.0.4-1mdk
- 1.4.0.4

* Fri Dec 31 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 1.4.0.3-3mdk
- revert latest "lib64 fixes"

* Tue Dec 28 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 1.4.0.3-2mdk
- lib64 fixes

* Fri Dec 17 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 1.4.0.3-1mdk
- 1.4.0.3

* Sat Nov 27 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 1.4.0.2-2mdk
- make it rpmbuildupdate aware

* Sat Nov 27 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 1.4.0.2-1mdk
- 1.4.0.2
- built against new shared ripole lib (P0)
- drop P1
- fix CFLAGS

* Mon Aug 30 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 1.4.0.1-1mdk
- 1.4.0.1
- fix P0
- add some header files

* Fri Dec 05 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 1.3.0.5-2mdk
- provide static and shared libs as well and build ripmime against it

* Sat Nov 15 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 1.3.0.5-1mdk
- 1.3.0.5

