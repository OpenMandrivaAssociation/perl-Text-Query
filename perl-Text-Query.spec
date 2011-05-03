%define upstream_name       Text-Query
%define upstream_version    0.07

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 7
Summary:	Query processing framework
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Text/%{upstream_name}-%{upstream_version}.tar.gz
Patch:      Text-Query-0.07-fix-syntax.patch
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This module provides an object that matches a data source against a query
expression.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 
%patch -p 1

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

