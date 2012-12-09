# revision 17476
# category Package
# catalog-ctan /graphics/pstricks/contrib/uml
# catalog-date 2010-03-17 12:19:20 +0100
# catalog-license lppl
# catalog-version 0.11
Name:		texlive-uml
Version:	0.11
Release:	2
Summary:	UML diagrams in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/uml
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uml.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uml.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uml.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.11-2
+ Revision: 757250
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.11-1
+ Revision: 719840
- texlive-uml
- texlive-uml
- texlive-uml

