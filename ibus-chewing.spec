%define	version 1.3.9.2
%define	release %mkrel 2

Name:      ibus-chewing
Summary:   ibus - Chinese chewing engine
Version:   %{version}
Release:   %{release}
Group:     System/Internationalization
License:   GPLv2+
URL:       http://code.google.com/p/ibus/
Source0:   http://ibus.googlecode.com/files/%name-%version-Source.tar.gz
Patch0:    ibus-chewing-1.3.9.2-build.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libxtst-devel
BuildRequires: libx11-devel
BuildRequires: libchewing-devel
BuildRequires: ibus-devel >= 1.3.9-5
BuildRequires: gtk2-devel
BuildRequires: gettext
BuildRequires: gob2
BuildRequires: GConf2
BuildRequires: cmake
Requires:	ibus >= 1.3.0
Requires:	libchewing-data
Requires(post): GConf2
Requires(preun): GConf2

%description
ibus - Chinese chewing engine.

%prep
%setup -q -n %name-%version-Source
%patch0 -p0 -b .build

%build
%cmake -DLIBEXEC_DIR="%{_libexecdir}"
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std -C build

rm -fr %buildroot%_datadir/doc

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%post_ibus_register_engine chewing zh_TW

%preun
%preun_uninstall_gconf_schemas %name
%preun_ibus_unregister_engine chewing

%files -f %name.lang
%defattr(-,root,root)
%{_sysconfdir}/gconf/schemas/*.schemas
%{_libexecdir}/ibus-engine-*
%{_datadir}/%name
%{_datadir}/ibus/component/*.xml
