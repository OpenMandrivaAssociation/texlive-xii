Name:		texlive-xii
Version:	45804
Release:	2
Summary:	Christmas silliness
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/plain/contrib/xii
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xii.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xii.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
TeXLive xii package.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/plain/xii

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
