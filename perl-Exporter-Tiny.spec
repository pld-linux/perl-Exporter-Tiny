#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Exporter
%define		pnam	Tiny
Summary:	Exporter::Tiny - an exporter with the features of Sub::Exporter but only core dependencies
Summary(pl.UTF-8):	Exporter::Tiny - eksporter o możliwościach Sub::Exportera, ale bez dużych zależności
Name:		perl-Exporter-Tiny
Version:	1.002001
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Exporter/Exporter-Tiny-%{version}.tar.gz
# Source0-md5:	e33f25f7556f5f5264a92cb9870d0eac
URL:		http://search.cpan.org/dist/Exporter-Tiny/
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.17
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-Fatal
BuildRequires:	perl-Test-Simple >= 0.47
BuildRequires:	perl-Test-Warnings
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Exporter::Tiny supports many of Sub::Exporter's external-facing
features including renaming imported functions with the -as, -prefix
and -suffix options; explicit destinations with the into option; and
alternative installers with the installler option. But it's written in
only about 40%% as many lines of code and with zero non-core
dependencies.

Its internal-facing interface is closer to Exporter.pm, with
configuration done through the @EXPORT, @EXPORT_OK and %%EXPORT_TAGS
package variables.

%description -l pl.UTF-8
Exporter::Tiny obsługuje wiele z zewnętrznych możliwości modułu
Sub::Exporter, w tym zmianę nazw importowanych funkcji przy użyciu
opcji -as, -prefix i -suffix; jawne cele przy użyciu opcji into;
alternatywne instalatory przy użyciu opcji installer. Jest natomiast
napisany w około 40%% liczby linii kodu i bez żadnych zależności
spoza głównej dystrybucji Perla.

Interfejs wewnętrzny jest zbliżony do interfejsu modułu Exporter.pm z
konfiguracją poprzez zmienne pakietu @EXPORT, @EXPORT_OK oraz
%%EXPORT_TAGS.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/Exporter/Tiny/Manual/*.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYRIGHT CREDITS Changes TODO
%{perl_vendorlib}/Exporter/Shiny.pm
%{perl_vendorlib}/Exporter/Tiny.pm
%{_mandir}/man3/Exporter::Shiny.3pm*
%{_mandir}/man3/Exporter::Tiny.3pm*
%{_mandir}/man3/Exporter::Tiny::Manual::*.3pm*
%{_examplesdir}/%{name}-%{version}
