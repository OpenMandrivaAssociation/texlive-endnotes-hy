Name:		texlive-endnotes-hy
Version:	54758
Release:	2
Summary:	Patches the endnotes package to create hypertext links to the correct anchors
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/endnotes-hy
License:	lppl1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/endnotes-hy.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/endnotes-hy.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/endnotes-hy.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package supports the creation of hypertext links in support
of the endnotes package. The package modifies the syntax of the
\endnote command: \endnote*[<num>]{<text>}\label{<name>}. When
the *-option is used, no endnote mark is created, but the
endnote itself is written. The \label command appears at the
end of the \endnote and its arguments, rather than within the
argument of the <text> argument.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/endnotes-hy
%{_texmfdistdir}/tex/latex/endnotes-hy
%doc %{_texmfdistdir}/doc/latex/endnotes-hy

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
