Summary:	CMake common macros for Eyescale projects
Summary(pl.UTF-8):	Wspólne makra CMake dla projektów Eyescale
Name:		Eyescale-CMake
Version:	2016.12
Release:	1
License:	BSD
Group:		Development/Tools
Source0:	https://github.com/Eyescale/CMake/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	29bbcd13dc912ed0c8fbfe474f050f2c
Patch0:		libdir.patch
URL:		https://github.com/Eyescale/CMake/
Requires:	cmake >= 2.8
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CMake common macros for Eyescale projects (like Lunchbox, Collage or
Equalizer).

%description -l pl.UTF-8
Wspólne makra CMake dla projektów Eyescale (takich jak Lunchbox,
Collage czy Equalizer).

%prep
%setup -q -n CMake-%{version}
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/Eyescale-CMake/common

cp -a * $RPM_BUILD_ROOT%{_datadir}/Eyescale-CMake/common
%{__rm} $RPM_BUILD_ROOT%{_datadir}/Eyescale-CMake/common/{CHANGES.md,LICENSE.txt,README.md}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.md LICENSE.txt README.md
%{_datadir}/Eyescale-CMake
