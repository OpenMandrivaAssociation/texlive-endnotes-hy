%global tl_name endnotes-hy
%global tl_revision 54758

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Patches the endnotes package to create hypertext links to the correct anchors
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/endnotes-hy
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/endnotes-hy.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/endnotes-hy.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/endnotes-hy.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package supports the creation of hypertext links in support of the
endnotes package. The package modifies the syntax of the \endnote
command: \endnote*[<num>]{<text>}\label{<name>}. When the *-option is
used, no endnote mark is created, but the endnote itself is written. The
\label command appears at the end of the \endnote and its arguments,
rather than within the argument of the <text> argument.

