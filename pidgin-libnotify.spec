%define version 0.13
%define release %mkrel 4
%define oldname gaim-libnotify

Summary:       Popup for Pidgin via libnotify and the notification-daemon
Name:          pidgin-libnotify
Version:       %{version}
Release:       %{release}
License:       GPL
Group:         Networking/Instant messaging
URL:           http://gaim-libnotify.sourceforge.net/
Source:        http://prdownloads.sourceforge.net/%{oldname}/%{name}-%{version}.tar.bz2
Patch0:        01-only_available.patch
Patch1:        02-fix_show_button.patch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: pidgin-devel
BuildRequires: gtk2-devel
BuildRequires: gettext-devel
BuildRequires: libsm-devel
BuildRequires: libnotify-devel
BuildRequires: autoconf2.5
BuildRequires: intltool
Requires:      pidgin

Obsoletes:     %{oldname}
Provides:      %{oldname}

%description
This plugin adds a libnotify interface to pidgin, enabling popups much like 
guifications. It has some configuration options, to show popups when a 
buddy signs on, on new messages and on new conversations only.

libnotify and notify-daemon aren't stable yet, so it's all very experimental.

Don't forget to enable the plugin in Tools->Plugins.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure2_5x --disable-deprecated
%make

%install
rm -rf %{buildroot}
%makeinstall_std
%find_lang %name
# remove files not bundled
rm -f %{buildroot}%{_libdir}/purple-2/*.{la,a}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog INSTALL README
%{_libdir}/purple-2/*.so
