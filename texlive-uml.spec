%global tl_name uml
%global tl_revision 17476

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.11
Release:	%{tl_revision}.1
Summary:	UML diagrams in LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pstricks/contrib/uml
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/uml.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/uml.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/uml.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A PSTricks related package for writing UML (Unified Modelling Language)
diagrams in LaTeX. Currently, it implements a subset of class diagrams,
and some extra constructs as well. The package cannot be used together
with pst-uml.

