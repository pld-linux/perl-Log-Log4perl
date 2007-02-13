#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Log
%define		pnam	Log4perl
Summary:	Log::Log4perl Perl module - adds logging capabilities
Summary(pl.UTF-8):	Moduł Perla Log::Log4perl - dostarczenie obsługi logowania
Name:		perl-Log-Log4perl
Version:	1.06
Release:	0.1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a7bda690ec0ad0bed457fa525e28034a
URL:		http://log4perl.sourceforge.net/
%if %{with tests}
BuildRequires:	perl-DBI
BuildRequires:	perl-DBD-CSV
BuildRequires:	perl-Log-Dispatch
BuildRequires:	perl-SQL-Statement
BuildRequires:	perl-XML-DOM >= 1.43
#BuildRequires:	perl-Log-Dispatch-FileRotate
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-XML-DOM >= 1.43
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# used conditionally
%define		_noautoreq	'perl(XML::DOM)' 'perl(LWP::UserAgent)' 'perl(Log::Dispatch::FileRotate).*'

%description
Log::Log4perl lets you remote-control and fine-tune the logging
behaviour of your system from the outside. It implements the widely
popular (Java-based) Log4j logging package in pure Perl.

%description -l pl.UTF-8
Log::Log4perl pozwala na zdalne sterowanie i szczegółowe dostosowanie
sposobu logowania z zewnątrz. Jest implementacją popularnego (opartego
na Javie) pakietu logującego Log4j w czystym Perlu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL < /dev/null \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/%{pdir}/*.pm
%{perl_vendorlib}/%{pdir}/%{pnam}
%{_mandir}/man3/*
