Summary:	CMake common macros for Eyescale projects
Summary(pl.UTF-8):	Wspólne makra CMake dla projektów Eyescale
Name:		Eyescale-CMake
Version:	2018.02
Release:	2
License:	BSD
Group:		Development/Tools
#Source0Download: https://github.com/Eyescale/CMake/releases
Source0:	https://github.com/Eyescale/CMake/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	3c20d5ad6dbbe95ca1119ad36ae5f8e1
Patch0:		libdir.patch
URL:		https://github.com/Eyescale/CMake/
BuildRequires:	sed >= 4.0
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

# python2 script (uses e.g. dict iteritems(), itervalues() methods)
%{__sed} -i -e '1s,/usr/bin/python$,%{__python},' util/cpplint.py

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/Eyescale-CMake

cp -a * $RPM_BUILD_ROOT%{_datadir}/Eyescale-CMake
%{__rm} $RPM_BUILD_ROOT%{_datadir}/Eyescale-CMake/{CHANGES.md,LICENSE.txt,README.md}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.md LICENSE.txt README.md
%{_datadir}/Eyescale-CMake
