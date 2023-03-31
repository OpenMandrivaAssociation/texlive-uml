Name:		texlive-uml
Version:	17476
Release:	2
Summary:	UML diagrams in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/uml
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uml.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uml.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uml.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A PSTricks related package for writing UML (Unified Modelling
Language) diagrams in LaTeX. Currently, it implements a subset
of class diagrams, and some extra constructs as well. The
package cannot be used together with pst-uml.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/uml/uml.sty
%doc %{_texmfdistdir}/doc/latex/uml/Changes
%doc %{_texmfdistdir}/doc/latex/uml/README
%doc %{_texmfdistdir}/doc/latex/uml/example.tex
%doc %{_texmfdistdir}/doc/latex/uml/uml.pdf
#- source
%doc %{_texmfdistdir}/source/latex/uml/Makefile
%doc %{_texmfdistdir}/source/latex/uml/uml.dtx
%doc %{_texmfdistdir}/source/latex/uml/uml.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
