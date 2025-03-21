Name:		fcitx5-lua
Version:	5.0.14
Release:	1
Source0:	https://github.com/fcitx/fcitx5-lua/archive/%{version}/%{name}-%{version}.tar.gz
Summary:	LUA scripting support for the fcitx input method system
URL:		https://github.com/fcitx/fcitx5-lua
License:	LGPL-2.1+
Group:		Graphical desktop/KDE
BuildRequires:	cmake
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Fcitx5Core)
BuildRequires:	cmake(Fcitx5ModuleQuickPhrase)
BuildRequires:	cmake(Fcitx5Module)
BuildRequires:	cmake(Fcitx5ModuleTestFrontend)
BuildRequires:	cmake(Fcitx5ModuleTestIM)
BuildRequires:	pkgconfig(lua)
BuildSystem:	cmake

%description
LUA scripting support for the fcitx input method system

%package devel
Summary:	Development files for the FCITX LUA plugin
Group:		Development/Libraries
Requires:	%{name} = %{EVRD}

%description devel
Development files for the FCITX LUA plugin

%files -f %{name}.lang
%{_libdir}/fcitx5/libluaaddonloader.so
%{_datadir}/fcitx5
%{_datadir}/metainfo/org.fcitx.Fcitx5.Addon.Lua.metainfo.xml

%files devel
%{_includedir}/Fcitx5/Module/fcitx-module/luaaddonloader
%{_libdir}/cmake/Fcitx5ModuleLuaAddonLoader
