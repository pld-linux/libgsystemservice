Summary:	Common components for building D-Bus system services
Summary(pl.UTF-8):	Wspólne komponenty do tworzenia usług systemowych D-Bus
Name:		libgsystemservice
Version:	0.2.0
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	https://download.gnome.org/sources/libgsystemservice/0.2/%{name}-%{version}.tar.xz
# Source0-md5:	e4ba190bf0ae40cf9b487a75abfc2b4c
URL:		https://gitlab.gnome.org/pwithnall/libgsystemservice
BuildRequires:	glib2-devel >= 1:2.71
BuildRequires:	gtk-doc
BuildRequires:	meson >= 0.54.0
BuildRequires:	ninja >= 1.5
BuildRequires:	polkit-devel >= 0.114
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	systemd-devel >= 1:209
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	glib2 >= 1:2.71
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libgsystemservice is a utility library providing common components
needed for building system services to be exposed on the D-Bus system
bus.

%description -l pl.UTF-8
libgsystemservice to biblioteka narzędziowa udostępniająca wspólne
komponenty potrzebne do tworzenia usług systemowych, udostępnianych
przez szynę systemową D-Bus.

%package devel
Summary:	Header files for libgsystemservice library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libgsystemservice
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.71
Requires:	systemd-devel >= 1:209

%description devel
Header files for libgsystemservice library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libgsystemservice.

%package static
Summary:	Static libgsystemservice library
Summary(pl.UTF-8):	Statyczna biblioteka libgsystemservice
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libgsystemservice library.

%description static -l pl.UTF-8
Statyczna biblioteka libgsystemservice.

%package apidocs
Summary:	API documentation for libgsystemservice library
Summary(pl.UTF-8):	Dokumentacja API biblioteki libgsystemservice
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for libgsystemservice library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libgsystemservice.

%prep
%setup -q

%build
%meson

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_libdir}/libgsystemservice-0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgsystemservice-0.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgsystemservice-0.so
%{_includedir}/gsystemservice-0
%{_pkgconfigdir}/gsystemservice-0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgsystemservice-0.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libgsystemservice
