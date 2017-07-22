#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-XML-SAX
Version  : 0.99
Release  : 7
URL      : http://search.cpan.org/CPAN/authors/id/G/GR/GRANTM/XML-SAX-0.99.tar.gz
Source0  : http://search.cpan.org/CPAN/authors/id/G/GR/GRANTM/XML-SAX-0.99.tar.gz
Summary  : ~
Group    : Development/Tools
License  : GPL-1.0
Requires: perl-XML-SAX-doc
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

%package doc
Summary: doc components for the perl-XML-SAX package.
Group: Documentation

%description doc
doc components for the perl-XML-SAX package.


%prep
%setup -q -n XML-SAX-0.99

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make V=1  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.0/XML/SAX.pm
/usr/lib/perl5/site_perl/5.26.0/XML/SAX/DocumentLocator.pm
/usr/lib/perl5/site_perl/5.26.0/XML/SAX/Intro.pod
/usr/lib/perl5/site_perl/5.26.0/XML/SAX/ParserFactory.pm
/usr/lib/perl5/site_perl/5.26.0/XML/SAX/PurePerl.pm
/usr/lib/perl5/site_perl/5.26.0/XML/SAX/PurePerl/DTDDecls.pm
/usr/lib/perl5/site_perl/5.26.0/XML/SAX/PurePerl/DebugHandler.pm
/usr/lib/perl5/site_perl/5.26.0/XML/SAX/PurePerl/DocType.pm
/usr/lib/perl5/site_perl/5.26.0/XML/SAX/PurePerl/EncodingDetect.pm
/usr/lib/perl5/site_perl/5.26.0/XML/SAX/PurePerl/Exception.pm
/usr/lib/perl5/site_perl/5.26.0/XML/SAX/PurePerl/NoUnicodeExt.pm
/usr/lib/perl5/site_perl/5.26.0/XML/SAX/PurePerl/Productions.pm
/usr/lib/perl5/site_perl/5.26.0/XML/SAX/PurePerl/Reader.pm
/usr/lib/perl5/site_perl/5.26.0/XML/SAX/PurePerl/Reader/NoUnicodeExt.pm
/usr/lib/perl5/site_perl/5.26.0/XML/SAX/PurePerl/Reader/Stream.pm
/usr/lib/perl5/site_perl/5.26.0/XML/SAX/PurePerl/Reader/String.pm
/usr/lib/perl5/site_perl/5.26.0/XML/SAX/PurePerl/Reader/URI.pm
/usr/lib/perl5/site_perl/5.26.0/XML/SAX/PurePerl/Reader/UnicodeExt.pm
/usr/lib/perl5/site_perl/5.26.0/XML/SAX/PurePerl/UnicodeExt.pm
/usr/lib/perl5/site_perl/5.26.0/XML/SAX/PurePerl/XMLDecl.pm

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man3/*
