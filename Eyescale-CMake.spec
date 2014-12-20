Summary:	CMake common macros for Eyescale projects
Summary(pl.UTF-8):	Wspólne makra CMake dla projektów Eyescale
Name:		Eyescale-CMake
Version:	0
%define	snap	20141214
%define	gitref	217fc77e74fa316bcaea12dc0df2919c08ce2231
Release:	0.%{snap}.1
License:	BSD
Group:		Development/Tools
Source0:	https://github.com/Eyescale/CMake/archive/%{gitref}/Eyescale-CMake-%{gitref}.tar.gz
# Source0-md5:	6a8afcf8f1f96dad07ae9e163a1b6786
Patch0:		Eyescale-cmake.patch
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
%setup -q -c
%{__mv} CMake-* common
%patch0 -p1

%{__rm} common/.gitignore
%{__mv} common/{CHANGES.md,LICENSE.txt,README.md} .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}

cp -a common $RPM_BUILD_ROOT%{_datadir}/Eyescale-CMake

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.md LICENSE.txt README.md
%{_datadir}/Eyescale-CMake
