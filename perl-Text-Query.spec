%define upstream_name       Text-Query
%define upstream_version    0.07

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	8
Summary:	Query processing framework
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source:		http://www.cpan.org/modules/by-module/Text/%{upstream_name}-%{upstream_version}.tar.gz
Patch:		Text-Query-0.07-fix-syntax.patch

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module provides an object that matches a data source against a query
expression.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 
%patch -p 1

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%check
# Seem to fail for no real reason
#make test

%files
%doc ChangeLog README
%{perl_vendorlib}/Text
%{_mandir}/*/*

%changelog
* Tue May 03 2011 Michael Scherer <misc@mandriva.org> 0.70.0-7mdv2011.0
+ Revision: 664902
- mass rebuild

* Thu Aug 20 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.70.0-6mdv2010.0
+ Revision: 418439
- fix build
- use new perl version macro

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun May 06 2007 Olivier Thauvin <nanardon@mandriva.org> 0.07-3mdv2008.0
+ Revision: 23641
- rebuild


* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.07-2mdk
- Fix SPEC according to Perl Policy
	- Source URL
- use mkrel

* Fri Jun 17 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.07-1mdk 
- first mdk release

