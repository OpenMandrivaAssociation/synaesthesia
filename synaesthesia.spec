%define name synaesthesia
%define version 2.4
%define release %mkrel 4

Name:          %{name}
Version:       %{version}
Release:       %{release}
Group:         Sound
Summary:       This program visualizes audio input
Source:        http://www.logarithmic.net/pfh-files/synaesthesia/%name-%version.tar.bz2
License:       GPL
Url:	       http://www.logarithmic.net/pfh-files/synaesthesia/
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: SDL1.2-devel 
BuildRequires: esound-devel

%description
This is a program for representing sounds visually.  It goes beyond
the usual oscilliscope style program by combining an FFT and stereo
positioning information to give a two dimensional display.

%prep

%setup -q
%build

%configure2_5x --disable-rpath

%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README COPYING
%{_bindir}/*


