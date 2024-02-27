%define _disable_lto 1
%define oname Drawpile

Name:           drawpile
Version:        2.2.1
Release:        1
Summary:        A collaborative drawing program
Group:          Graphics/Editors and Converters
License:        GPLv3+
URL:            https://drawpile.net/
Source0:         https://github.com/drawpile/Drawpile/archive/%{version}/%{oname}-%{version}.tar.gz
Source1:        vendor.tar.xz
Source2:        cargo_config
#Patch0:		drawpile-2.2-static-helpers.patch

BuildRequires:  cmake
BuildRequires:	cmake(ECM)
BuildRequires:	ninja
BuildRequires:  cargo
BuildRequires:  rust
BuildRequires:  desktop-file-utils
BuildRequires:  xdg-utils
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5DNSSD)
BuildRequires:	qt5-qttools
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
BuildRequires:	pkgconfig(libsodium)
BuildRequires:  pkgconfig(libmypaint)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  miniupnpc-devel
#Optional
BuildRequires:	pkgconfig(vpx)
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
%autosetup -n %{oname}-%{version} -a1 -p1
mkdir .cargo
cp %{SOURCE2} .cargo/config
%cmake \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
#doc %{_docdir}/%{name}/
%{_bindir}/drawpile*
%{_datadir}/drawpile/
%{_datadir}/metainfo/net.drawpile.drawpile.appdata.xml
%{_datadir}/applications/net.drawpile.drawpile.desktop
%{_datadir}/mime/application/vnd.drawpile.recording.xml
%{_datadir}/mime/text/vnd.drawpile.recording.xml
%{_iconsdir}/hicolor/*/apps/drawpile*
%{_iconsdir}/hicolor/*/mimetypes/*
