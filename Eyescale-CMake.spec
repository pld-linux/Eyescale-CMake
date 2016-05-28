Summary:	CMake common macros for Eyescale projects
Summary(pl.UTF-8):	Wspólne makra CMake dla projektów Eyescale
Name:		Eyescale-CMake
Version:	2016.04
%define	gitref	0e519bfbbf74bb30a17c75d5c4c4d0266f5d272b
Release:	1
License:	BSD
Group:		Development/Tools
Source0:	https://github.com/Eyescale/CMake/archive/%{gitref}/Eyescale-CMake-%{gitref}.tar.gz
# Source0-md5:	b121851bcee76d6e99abdacf54a4512c
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
