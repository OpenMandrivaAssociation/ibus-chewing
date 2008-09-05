%define snapdate 20080905
%define	version 0.1.1.%{snapdate}
%define	release %mkrel 1

Name:      ibus-chewing
Summary:   ibus - Chinese chewing engine
Version:   %{version}
Release:   %{release}
Group:     System/Internationalization
License:   GPLv2+
URL:       http://code.google.com/p/ibus/
# fwang: generated from libchewing_svn branch
Source0:   %{name}-%{snapdate}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libchewing-devel
BuildRequires: python-devel
BuildRequires: gettext-devel
BuildRequires: swig
Requires:	ibus
Requires:	libchewing-data

%description
ibus - Chinese chewing engine.

%prep
%setup -q -n %{name}-%{snapdate}

%build
./autogen.sh
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root)
%{_bindir}/*
%{_datadir}/%{name}
%{python_sitearch}/*
%{_datadir}/ibus/engine/*.engine
