%define	version 1.2.99.20100317
%define	release %mkrel 1

Name:      ibus-chewing
Summary:   ibus - Chinese chewing engine
Version:   %{version}
Release:   %{release}
Group:     System/Internationalization
License:   GPLv2+
URL:       http://code.google.com/p/ibus/
Source0:   http://ibus.googlecode.com/files/%name-%version-Source.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libxtst-devel
BuildRequires: libx11-devel
BuildRequires: libchewing-devel
BuildRequires: ibus-devel >= 1.2.0
BuildRequires: gtk2-devel
BuildRequires: gettext
BuildRequires: gob2
BuildRequires: cmake
Requires:	ibus >= 1.2.0
Requires:	libchewing-data

%description
ibus - Chinese chewing engine.

%prep
%setup -q -n %name-%version-Source

%build
%cmake -DLIBEXEC_DIR="%{_libdir}"
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
%{_sysconfdir}/gconf/schemas/*.schemas
%{_libexecdir}/ibus-engine-*
%{_datadir}/%name
%{_datadir}/ibus/component/*.xml
