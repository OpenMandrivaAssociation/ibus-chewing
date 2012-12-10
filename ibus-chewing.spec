Name:		ibus-chewing
Summary:	ibus - Chinese chewing engine
Version:	1.4.3
Release:	1
Group:		System/Internationalization
License:	GPLv2+
URL:		http://code.google.com/p/ibus/
Source0:	http://ibus.googlecode.com/files/%{name}-%{version}-Source.tar.gz
Source1:	https://fedorahosted.org/releases/c/m/cmake-fedora/cmake-fedora-modules-only-latest.tar.gz
Patch0:		ibus-chewing-1.4.0-build.patch
BuildRequires:	pkgconfig(xtst)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(chewing)
BuildRequires:	pkgconfig(ibus-1.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	gettext
BuildRequires:	gob2
BuildRequires:	cmake
BuildRequires:	GConf2
Requires:	ibus >= 1.3.0
Requires:	libchewing-data
Requires(post):	GConf2
Requires(preun): GConf2

%description
ibus - Chinese chewing engine.

%prep
%setup -q -n %{name}-%{version}-Source -a1
%patch0 -p0 -b .orig

%build
%setup_compile_flags
cmake -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} -DLIBEXEC_DIR="%{_libexecdir}" -DSYSCONF_INSTALL_DIR:PATH=%{_sysconfdir}
%make

%install
%makeinstall_std

rm -fr %{buildroot}%{_datadir}/doc

%find_lang %{name}

%preun
%preun_uninstall_gconf_schemas %{name}

%files -f %{name}.lang
%{_sysconfdir}/gconf/schemas/*.schemas
%{_libexecdir}/ibus-engine-*
%{_datadir}/%{name}
%{_datadir}/ibus/component/*.xml

