Name:           drawpile
Version:        2.1.11
Release:        1
Summary:        A collaborative drawing program
Group:          Graphics/Editors and Converters
License:        GPLv3+
URL:            https://drawpile.net/
Source:         https://github.com/drawpile/Drawpile/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  xdg-utils
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5DNSSD)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Help)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(libmicrohttpd)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  giflib-devel
BuildRequires:  miniupnpc-devel

%description
Drawpile is a drawing program that lets you share the canvas with other users in real time.
Some feature highlights:

    Runs on Linux, Windows and OSX
    Shared canvas using the built-in server or a dedicated server
    Record, play back and export drawing sessions
    Simple animation support
    Layers and blending modes
    Text layers
    Supports pressure sensitive Wacom tablets
    Built-in chat
    Supports OpenRaster file format
    Encrypted connections using SSL
    Automatic port forwarding with UPnP


%prep
%setup -qn Drawpile-%{version}
%autopatch -p1

%build
%cmake_qt5
%make_build

%install
%make_install -C build

#fix .desktop file
desktop-file-edit \
	--remove-category=Network \
		%{buildroot}%{_datadir}/applications/drawpile.desktop

%files
%doc %{_docdir}/%{name}/
%{_bindir}/drawpile*
%{_datadir}/drawpile/
%{_datadir}/appdata/drawpile.appdata.xml
%{_datadir}/applications/drawpile.desktop
%{_datadir}/mime/packages/x-drawpile.xml
%{_iconsdir}/hicolor/*/apps/drawpile*
%{_iconsdir}/hicolor/*/mimetypes/*
%{_mandir}/man1/drawpile*
