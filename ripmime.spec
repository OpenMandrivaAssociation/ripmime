%define	major 1
%define libname	%mklibname ripmime %{major}

Summary:	Extracts attachments out of mailpack format emails
Name:		ripmime
Version:	1.4.0.7
Release:	%mkrel 0.dev.1
License:	BSD
Group:		Networking/Mail
URL:		http://www.pldaniels.com/ripmime/
Source0:	http://www.pldaniels.com/ripmime/%{name}-1.4.0.6.tar.bz2
Patch0:		ripmime-1.4.0.6-shared.diff
Patch1:		ripmime-1.4-dev.diff
BuildRequires:	libtool
BuildRequires:	libripole-devel
BuildRoot:	%{_tmppath}/%{name}-buildroot

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

%package -n	%{libname}-devel
Summary:	Development files for the %{name} library
Group:		Development/C
Provides:	%{name}-devel = %{version}
Provides:	lib%{name}-devel = %{version}
Requires:	%{libname} = %{version}

%description -n	%{libname}-devel
ripMIME is a small program which has been developed as part of the
commercial Xamime development (http://www.xamime.com).

ripMIME has been written with one sole purpose in mind, to extract
the attached files out of a MIME encoded email package.

This package provides development files for the %{name} library.

%prep

%setup -q -n %{name}-1.4.0.6
%patch0 -p0
%patch1 -p1

%build

%make \
    CFLAGS="%{optflags}" \
    libdir=%{_libdir}

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std \
    bindir=%{_bindir} \
    includedir=%{_includedir} \
    libdir=%{_libdir} \
    mandir=%{_mandir}

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGELOG CONTRIBUTORS INSTALL LICENSE README
%{_bindir}/*
%{_mandir}/man1/*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%doc TODO
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la

