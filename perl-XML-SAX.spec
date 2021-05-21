#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-XML-SAX
Version  : 1.02
Release  : 27
URL      : https://cpan.metacpan.org/authors/id/G/GR/GRANTM/XML-SAX-1.02.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/G/GR/GRANTM/XML-SAX-1.02.tar.gz
Summary  : unknown
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-XML-SAX-license = %{version}-%{release}
Requires: perl-XML-SAX-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(XML::NamespaceSupport)
BuildRequires : perl(XML::SAX::Base)
BuildRequires : perl(XML::SAX::Exception)

%description
XML::SAX
========
XML::SAX consists of several framework classes for using and building
Perl SAX2 XML parsers, filters, and drivers. It is designed around the
need to be able to "plug in" different SAX parsers to an application
without requiring programmer intervention. Those of you familiar with
the DBI will be right at home. Some of the designs come from the Java
JAXP specification (SAX part), only without the javaness.

%package dev
Summary: dev components for the perl-XML-SAX package.
Group: Development
Provides: perl-XML-SAX-devel = %{version}-%{release}
Requires: perl-XML-SAX = %{version}-%{release}

%description dev
dev components for the perl-XML-SAX package.


%package license
Summary: license components for the perl-XML-SAX package.
Group: Default

%description license
license components for the perl-XML-SAX package.


%package perl
Summary: perl components for the perl-XML-SAX package.
Group: Default
Requires: perl-XML-SAX = %{version}-%{release}

%description perl
perl components for the perl-XML-SAX package.


%prep
%setup -q -n XML-SAX-1.02
cd %{_builddir}/XML-SAX-1.02

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-XML-SAX
cp %{_builddir}/XML-SAX-1.02/LICENSE %{buildroot}/usr/share/package-licenses/perl-XML-SAX/ce714346889d1becdd3132cf7380c734a985ecf1
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/XML::SAX.3
/usr/share/man/man3/XML::SAX::DocumentLocator.3
/usr/share/man/man3/XML::SAX::Intro.3
/usr/share/man/man3/XML::SAX::ParserFactory.3
/usr/share/man/man3/XML::SAX::PurePerl.3
/usr/share/man/man3/XML::SAX::PurePerl::Reader.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-XML-SAX/ce714346889d1becdd3132cf7380c734a985ecf1

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/XML/SAX.pm
/usr/lib/perl5/vendor_perl/5.34.0/XML/SAX/DocumentLocator.pm
/usr/lib/perl5/vendor_perl/5.34.0/XML/SAX/Intro.pod
/usr/lib/perl5/vendor_perl/5.34.0/XML/SAX/ParserFactory.pm
/usr/lib/perl5/vendor_perl/5.34.0/XML/SAX/PurePerl.pm
/usr/lib/perl5/vendor_perl/5.34.0/XML/SAX/PurePerl/DTDDecls.pm
/usr/lib/perl5/vendor_perl/5.34.0/XML/SAX/PurePerl/DebugHandler.pm
/usr/lib/perl5/vendor_perl/5.34.0/XML/SAX/PurePerl/DocType.pm
/usr/lib/perl5/vendor_perl/5.34.0/XML/SAX/PurePerl/EncodingDetect.pm
/usr/lib/perl5/vendor_perl/5.34.0/XML/SAX/PurePerl/Exception.pm
/usr/lib/perl5/vendor_perl/5.34.0/XML/SAX/PurePerl/NoUnicodeExt.pm
/usr/lib/perl5/vendor_perl/5.34.0/XML/SAX/PurePerl/Productions.pm
/usr/lib/perl5/vendor_perl/5.34.0/XML/SAX/PurePerl/Reader.pm
/usr/lib/perl5/vendor_perl/5.34.0/XML/SAX/PurePerl/Reader/NoUnicodeExt.pm
/usr/lib/perl5/vendor_perl/5.34.0/XML/SAX/PurePerl/Reader/Stream.pm
/usr/lib/perl5/vendor_perl/5.34.0/XML/SAX/PurePerl/Reader/String.pm
/usr/lib/perl5/vendor_perl/5.34.0/XML/SAX/PurePerl/Reader/URI.pm
/usr/lib/perl5/vendor_perl/5.34.0/XML/SAX/PurePerl/Reader/UnicodeExt.pm
/usr/lib/perl5/vendor_perl/5.34.0/XML/SAX/PurePerl/UnicodeExt.pm
/usr/lib/perl5/vendor_perl/5.34.0/XML/SAX/PurePerl/XMLDecl.pm
