
%define		sname	gift-openft

Summary:	The generic interface to FastTrack: OpenFT plugin
Summary(pl):	Interfejs do FastTracka: wtyczka OpenFT
Name:		giFT-openft
Version:	0.2.1.5
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/gift/%{sname}-%{version}.tar.bz2
# Source0-md5:	43286096e9e6e94c6a5f0da236eb4d14
URL:		http://giFT.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	db-devel
BuildRequires:	giFT-devel >= 0.11.4
BuildRequires:	libmagic-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The generic interface to FastTrack network. This package contains
OpenFT plugin.

%description -l pl
Ogólny interfejs do sieci FastTrack. Ten pakiet zawiera wtyczkê dla
sieci OpenFT.

%prep
%setup -q -n %{sname}-%{version}

%build
rm -f missing
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README AUTHORS TODO ChangeLog
%attr(755,root,root) %{_libdir}/giFT/*.so
%{_libdir}/giFT/*.la
%{_datadir}/giFT/*
