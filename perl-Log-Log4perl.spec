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
Version:	1.46
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d247d2327d7f32dca09cbeb51a953fc5
URL:		http://mschilli.github.io/log4perl/
%if %{with tests}
BuildRequires:	perl(File::Path) >= 2.06_06
BuildRequires:	perl(File::Spec) >= 0.82
BuildRequires:	perl-DBD-CSV >= 0.33
BuildRequires:	perl-DBD-SQLite
BuildRequires:	perl-DBI >= 1.607
BuildRequires:	perl-Log-Dispatch
#BuildRequires:	perl-Log-Dispatch-FileRotate >= 1.10
BuildRequires:	perl-SQL-Statement >= 1.20
BuildRequires:	perl-Test-Simple >= 0.45
BuildRequires:	perl-XML-DOM >= 1.43
#BuildRequires:	perl-rrdtool
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.663
Requires:	perl-XML-DOM >= 1.43
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# used conditionally
%define		_noautoreq_perl	XML::DOM LWP::UserAgent Log::Dispatch::FileRotate Log::Log4Perl.* RRDs

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
%doc Changes LICENSE
%attr(755,root,root) %{_bindir}/l4p-tmpl
%{perl_vendorlib}/Log/Log4perl.pm
%{perl_vendorlib}/Log/Log4perl
%{_mandir}/man1/l4p-tmpl.1p*
%{_mandir}/man3/Log::Log4perl*.3pm*
