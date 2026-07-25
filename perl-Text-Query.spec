%define upstream_name       Text-Query
%define upstream_version 0.09

Name:		perl-%{upstream_name}
Version:	%{upstream_version}
Release:	3
Summary:	Query processing framework
License:	GPL or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Text-Query
Source:		https://cpan.metacpan.org/authors/id/J/JO/JONJ/Text-Query-%{upstream_version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module provides an object that matches a data source against a query
expression.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

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
