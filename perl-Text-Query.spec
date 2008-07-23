%define module	Text-Query
%define name	perl-%{module}
%define version 0.07
%define release %mkrel 5

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Query processing framework
License:	GPL or Artistic
Group:		Development/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Text/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This module provides an object that matches a data source against a query
expression.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%check
make test

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog README
%{perl_vendorlib}/Text
%{_mandir}/*/*

