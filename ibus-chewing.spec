%define	version 1.0.0.20090220
%define	release %mkrel 1

Name:      ibus-chewing
Summary:   ibus - Chinese chewing engine
Version:   %{version}
Release:   %{release}
Group:     System/Internationalization
License:   GPLv2+
URL:       http://code.google.com/p/ibus/
Source0:   http://ibus.googlecode.com/files/%name-%version-Source.tar.gz
Patch0:	   ibus-chewing-1.0.0-fix-build.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libchewing-devel
BuildRequires: ibus-devel >= 1.1.0
BuildRequires: gettext
BuildRequires: gob2
BuildRequires: cmake
Requires:	ibus >= 1.1.0
Requires:	libchewing-data

%description
ibus - Chinese chewing engine.

%prep
%setup -q -n %name-%version-Source
%patch0 -p0

%build
%cmake
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std -C build

rm -fr %buildroot%_datadir/doc

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root)
%{_libexecdir}/ibus-engine-*
%{_datadir}/%name
%{_datadir}/ibus/component/*.xml
