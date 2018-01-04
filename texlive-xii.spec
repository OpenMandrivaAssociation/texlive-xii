# revision 31683
# category Package
# catalog-ctan /macros/plain/contrib/xii
# catalog-date 2013-09-17 19:06:55 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-xii
Version:	20171115
Release:	1
Summary:	Christmas silliness
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/plain/contrib/xii
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xii.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xii.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
