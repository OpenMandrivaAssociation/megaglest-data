Name:		megaglest-data
Version:	3.7.1
Release:	1
Summary:	Mega Glest data files
License:	Creative Commons Attribution
Group:		Games/Strategy
Url:		http://megaglest.org/
Source0:	http://downloads.sourceforge.net/project/megaglest/megaglest_%{version}/%{name}-%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	cmake

%description
MegaGlest is an open source 3D-real-time strategy game, where you control
the armies of one of seven different factions: Tech, Magic, Egyptians,
Indians, Norsemen, Persian or Romans. The game is setup in one of 16
naturally looking settings, which -like the unit models- are crafted with
great appreciation for detail. Additional game data can be downloaded from
within the game at no cost.

#-----------------------------------------------------------------------
%prep
%setup -q -n megaglest-%{version}

#-----------------------------------------------------------------------
%build
%cmake									\
	-DCMAKE_INSTALL_PREFIX=/					\
	-DMEGAGLEST_BIN_INSTALL_PATH=%{_gamesbindir}			\
	-DMEGAGLEST_ICON_INSTALL_PATH=%{_iconsdir}			\
	-DMEGAGLEST_DATA_INSTALL_PATH=%{_gamesdatadir}/megaglest
%make

#-----------------------------------------------------------------------
%install
%makeinstall_std -C build
rm -fr %{buildroot}%{_gamesdatadir}/megaglest/docs

#-----------------------------------------------------------------------
%files
%doc docs/*
%{_gamesdatadir}/megaglest


%changelog
* Wed Jan 02 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 3.7.1-1
- Update to latest upstream release.

* Sat Jan 28 2012 Paulo Andrade <pcpa@mandriva.com.br> 3.6.0.3-0.1mdv2012.0
+ Revision: 769484
- Update to latest upstream release.

* Sun Dec 18 2011 Paulo Andrade <pcpa@mandriva.com.br> 3.6.0-0.1
+ Revision: 743595
- Update to latest upstream release.

  + Zombie Ryushu <ryushu@mandriva.org>
    - Fix release tag for 2010.2 backport

* Thu Sep 08 2011 Paulo Andrade <pcpa@mandriva.com.br> 3.5.2.4-1
+ Revision: 698915
- MegaGlest 3.5.2.4 data files
- MegaGlest 3.5.2.4 data files

