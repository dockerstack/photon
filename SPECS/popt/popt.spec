Summary:	Programs to parse command-line options
Name:		popt
Version:	1.16
Release:	1
License:	MIT
URL:		http://rpm5.org/files/popt
Group:		Applications/System
Vendor:		VMware, Inc.
Distribution: 	Photon
Source0:	ftp://anduin.linuxfromscratch.org/BLFS/svn/p/%{name}-%{version}.tar.gz
%description
The popt package contains the popt libraries which are used by
some programs to parse command-line options.

%package devel
Summary:	Libraries and header files for popt
Requires:	%{name} = %{version}

%description devel
Static libraries and header files for the support library for popt

%prep
%setup -q
%build
./configure \
	--prefix=%{_prefix} \
	--bindir=%{_bindir} \
	--disable-silent-rules
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
find %{buildroot} -name '*.la' -delete
%find_lang %{name}
%check
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%files -f %{name}.lang
%defattr(-,root,root)
%{_libdir}/libpopt.so.*
%{_mandir}/*/*

%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/pkgconfig/popt.pc
%{_libdir}/libpopt.a
%{_libdir}/libpopt.so

%changelog
*	Wed Nov 5 2014 Divya Thaluru <dthaluru@vmware.com> 1.16-1
-	Initial build.	First version	
