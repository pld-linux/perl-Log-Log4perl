
# Conditional build:
%bcond_without tests	# do not perform "make test"

%include	/usr/lib/rpm/macros.perl
%define	pdir	Log
%define	pnam	Log4perl
Summary:	Log::Log4perl module adds logging capabilities
Summary(pl):	Modu� Log::Log4perl dostarczaj�cy obs�ug� logowania
Name:		perl-%{pdir}-%{pnam}
Version:	0.39
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	337e1382b600da2c8c6223cb0413a2de
URL:		http://log4perl.sourceforge.net/
%if %{with tests}
BuildRequires:	perl-DBI
BuildRequires:	perl-DBD-CSV
BuildRequires:	perl-Log-Dispatch
BuildRequires:	perl-XML-DOM >= 1.43
#BuildRequires:	perl-Log-Dispatch-FileRotate
%endif
BuildRequires:	perl-devel >= 5.6
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

%description -l pl
Log::Log4perl pozwala na zdalne sterowanie i szczeg�owe dostosowanie
sposobu logowania z zewn�trz. Jest implementacj� popularnego (opartego
na Javie) pakietu loguj�cego Log4j w czystym Perlu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL < /dev/null \
        INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/%{pdir}/*.pm
%{perl_vendorlib}/%{pdir}/%{pnam}
%{_mandir}/man3/*
