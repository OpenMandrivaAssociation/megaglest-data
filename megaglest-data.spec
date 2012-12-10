Name:		megaglest-data
Version:	3.6.0.3
Release:	%mkrel 0.1
Summary:	Mega Glest data files
License:	Creative Commons Attribution
Group:		Games/Strategy
Url:		http://megaglest.org/
Source0:	http://sourceforge.net/projects/megaglest/files/current_release/megaglest-data-3.6.0.3.tar.xz
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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

#-----------------------------------------------------------------------
%files
%defattr(644,root,root,755)
%{_gamesdatadir}/megaglest


%changelog
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

