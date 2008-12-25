%define	version 0.1.1.20081023
%define	release %mkrel 2

Name:      ibus-chewing
Summary:   ibus - Chinese chewing engine
Version:   %{version}
Release:   %{release}
Group:     System/Internationalization
License:   GPLv2+
URL:       http://code.google.com/p/ibus/
Source0:   http://ibus.googlecode.com/files/%name-%version.tar.gz
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
%setup -q

%build
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
