Summary:	ibus - Chinese chewing engine
Name:		ibus-chewing
Version:	1.4.7
Release:	2
License:	GPLv2+
Group:		System/Internationalization
Url:		https://code.google.com/p/ibus/
Source0:	http://ibus.googlecode.com/files/%{name}-%{version}-Source.tar.gz
Source1:	https://fedorahosted.org/releases/c/m/cmake-fedora/cmake-fedora-modules-only-latest.tar.gz
BuildRequires:	cmake
BuildRequires:	GConf2
BuildRequires:	gettext
BuildRequires:	gob2
BuildRequires:	pkgconfig(chewing)
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(ibus-1.0)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xtst)
Requires:	ibus >= 1.3.0
Requires:	libchewing-data
Requires(post,preun):	GConf2

%description
ibus - Chinese chewing engine.

%files -f %{name}.lang
%{_sysconfdir}/gconf/schemas/*.schemas
%{_libexecdir}/ibus-engine-*
%{_datadir}/%{name}
%{_datadir}/ibus/component/*.xml

#----------------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{version}-Source -a1

%build
%setup_compile_flags
cmake -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} -DLIBEXEC_DIR="%{_libexecdir}" -DSYSCONF_INSTALL_DIR:PATH=%{_sysconfdir}
%make
%make translations

%install
%makeinstall_std

rm -fr %{buildroot}%{_datadir}/doc

%find_lang %{name}

