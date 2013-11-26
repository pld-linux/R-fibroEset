%define		packname	fibroEset

Summary:	exprSet for Karaman et al. (2003) fibroblasts data
Name:		R-%{packname}
Version:	1.4.10
Release:	1
License:	LGPL
Group:		Applications/Engineering
Source0:	http://www.bioconductor.org/packages/release/data/experiment/src/contrib/%{packname}_%{version}.tar.gz
# Source0-md5:	0aff08f83abab03a3615800c421877bf
URL:		http://www.bioconductor.org/packages/release/data/experiment/html/fibroEset.html
BuildRequires:	R-Biobase
BuildRequires:	R
BuildRequires:	texlive-latex
Requires:	R-Biobase
Requires:	R
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
exprSet for Karaman et al. (2003) human, bonobo and gorilla
fibroblasts data.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library

R CMD INSTALL %{packname} -l $RPM_BUILD_ROOT%{_libdir}/R/library

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_libdir}/R/library/%{packname}/
%doc %{_libdir}/R/library/%{packname}/DESCRIPTION
%doc %{_libdir}/R/library/%{packname}/html/
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/Meta/
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/R/
%{_libdir}/R/library/%{packname}/help/
%{_libdir}/R/library/%{packname}/data
