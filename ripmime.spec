%define	major 1
%define libname %mklibname ripmime %{major}
%define develname %mklibname ripmime -d

Summary:	Extracts attachments out of mailpack format emails
Name:		ripmime
Version:	1.4.0.7
Release:	%mkrel 2
License:	BSD
Group:		Networking/Mail
URL:		http://www.pldaniels.com/ripmime/
Source0:	http://www.pldaniels.com/ripmime/%{name}-%{version}.tar.gz
Patch0:		ripmime-shared.diff
BuildRequires:	libtool
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
Requires:	%{libname} = %{version}
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

%build
%serverbuild

%make \
    CFLAGS="$CFLAGS" \
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

%files -n %{develname}
%defattr(-,root,root)
%doc TODO
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
