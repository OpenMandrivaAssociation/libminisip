%define name	libminisip
%define oname	minisip
%define version 0.3.1
%define svn	3565
%define release %mkrel %svn.2

%define major	0
%define libname %mklibname %{oname} %major
%define develname %mklibname %{oname} -d

Summary: 	MiniSip library from MiniSip
Name: 	 	%{name}
Version: 	%{version}
Release: 	%{release}
License:	GPL
Group:		System/Libraries
URL:		https://www.minisip.org/
Source:		http://www.minisip.org/source/%{name}-%{svn}.tar.bz2
BuildRequires:	libmstun-devel >= 0.5.0-3565.0
BuildRequires:	libmnetutil-devel >= 0.3.1-3565.0
BuildRequires:	libmikey-devel >= 0.4.1-3565.0
BuildRequires:	libmsip-devel >= 0.3.1-3565.0
BuildRequires:	ffmpeg-devel
BuildRequires:	SDL-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	libGConf2-devel
BuildRequires:	libdc1394-devel
BuildRequires:	libffmpeg-devel
BuildRequires:	libgsm-devel
BuildRequires:	libportaudio-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	libspeex-devel
BuildRequires:	libzrtpcpp-devel
BuildRequires:	zlib-devel
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
MiniSip library from MiniSip

%package	plugins
Summary:	Plugins from libminisip
Group:		System/Libraries

%description	plugins
Plugins from libminisip

%package -n 	%{libname}
Summary:        Dynamic libraries from %{name}
Group:          System/Libraries
Requires:	%{name}-plugins
Provides:       %{name} = %{version}-%{release}

%description -n %{libname}
Dynamic libraries from %{name}.

%package -n 	%{develname}
Summary: 	Header files and static libraries from %{name}
Group: 		Development/C
Requires: 	%{libname} >= %{version}
Provides:	%{name}-devel = %{version}-%{release} 

%description -n %{develname}
Libraries and includes files for developing programs based on %{name}.

%prep

%setup -q -n %{name}

%build
./bootstrap
%configure2_5x \
    --enable-alsa \
    --enable-gconf \
    --enable-portaudio \
    --enable-sdl \
    --enable-video \
    --enable-zrtp \
    --with-avcodec=%{_includedir}/ffmpeg

perl -pi -e 's|-lnsl|-lnsl -lpthread||g' Makefile

%make
										
%install
rm -rf %{buildroot}

%makeinstall

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{major}.*

%files plugins
%defattr(-,root,root)
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%{_libdir}/%{name}/plugins/*.so

%files -n %{develname}
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README 
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc
%{_datadir}/aclocal/*.m4
%{_libdir}/%{name}/plugins/*.a
%{_libdir}/%{name}/plugins/*.la
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la


