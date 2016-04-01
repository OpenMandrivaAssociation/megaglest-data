Name:		megaglest-data
Version:	3.12.0
Release:	1
Summary:	Mega Glest data files
License:	Creative Commons Attribution
Group:		Games/Strategy
Url:		http://megaglest.org/
Source0:	https://github.com/MegaGlest/megaglest-data/releases/download/%{version}/%{name}-%{version}.b1.tar.xz
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
	-DMEGAGLEST_BIN_INSTALL_PATH=%{_gamesbindir}			\
	-DMEGAGLEST_ICON_INSTALL_PATH=%{_datadir}/icons/hicolor/48x48/apps	\
	-DMEGAGLEST_DATA_INSTALL_PATH=%{_datadir}/games/megaglest
%make

#-----------------------------------------------------------------------
%install
%makeinstall_std -C build
rm -fr %{buildroot}%{_gamesdatadir}/megaglest/docs

rm -f %{buildroot}%{_iconsdir}/hicolor/48x48/apps/megaglest.xpm

# Remove unused Debian menu
rm -rf %{buildroot}%{_datadir}/menu

#-----------------------------------------------------------------------
%files
%doc docs/*
%{_gamesdatadir}/megaglest
%{_datadir}/appdata/megaglest*.appdata.xml
%{_datadir}/applications/megaglest*.desktop
%{_iconsdir}/hicolor/48x48/apps/megaglest.png
