%define name xmms-crystality
%define oname crystality-plugin
%define version 0.92
%define release %mkrel 10

Summary: Realtime plugin for remastering mp3 sound
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{oname}-%{version}.tar.bz2
Patch: crystality-plugin-0.92-optflags.patch
Patch1: crystality-plugin-0.92-fix-crash.patch
Patch2: crystality-plugin-0.92-gcc3.3.patch
License: GPL
Group: Sound
BuildRoot: %{_tmppath}/%{name}-buildroot
Requires: xmms
BuildRequires: libxmms-devel
URL: http://fanthom.math.put.poznan.pl/~gyver/crystality/

%description

This software consists of XMMS plugin and stdin/stdout plugin. It was
written for realtime remastering of sound from mp3 files.  You will
need a reasonably good stereo and a good ear to notice quality
improvement, otherwise this is not for you.  This plugin tries to
patch mp3 format flaws, not a poor audio hardware!  Yes, you should be
able to hear well enough (sorry) - for some of my friends plugin is a
cool thing, while the others does not hear nothing but echo and stereo
expander (well, you will hear every effect if you set it to the
maximum, but it will not sound nice).


%prep
%setup -q -n %oname-%version
%patch
%patch1
%patch2 -p1

%build
%make clean all OPTFLAGS="%optflags -fPIC"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %buildroot/%_libdir/xmms/Effect %buildroot/%_bindir
cp crystality-stdio %buildroot/%_bindir
cp libcrystality.so %buildroot/%_libdir/xmms/Effect
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README COPYING ChangeLog
%_bindir/crystality-stdio
%_libdir/xmms/Effect/libcrystality.so


