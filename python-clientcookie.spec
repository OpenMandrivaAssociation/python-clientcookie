%define oname ClientCookie
%define version 1.3.0
%define unmangled_version 1.3.0
%define unmangled_version 1.3.0
%define release 7

Summary: Client-side HTTP cookie handling
Name: python-clientcookie
Version: %{version}
Release: %{release}
Source0: %{oname}-%{unmangled_version}.tar.gz
License: BSD
Group: Development/Python
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
BuildRequires: python-devel
BuildRequires: python-setuptools
Url: https://wwwsearch.sourceforge.net/ClientCookie/

%description
ClientCookie is a Python module for handling HTTP cookies on the
client side, useful for accessing web sites that require cookies to be
set and then returned later.  It also provides some other (optional)
useful stuff: HTTP-EQUIV and Refresh handling, automatic adding of the
Referer [sic] header, robots.txt observance and lazily-seek()able
responses.  These extras are implemented using an extension that makes
it easier to add new functionality to urllib2 (now part of urllib2, as
of Python 2.4).  It has developed from a port of Gisle Aas' Perl
module HTTP::Cookies, from the libwww-perl library.


%prep
%setup -q -n %{oname}-%{unmangled_version} -n %{oname}-%{unmangled_version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --single-version-externally-managed --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc *.txt *.html
%py_puresitedir/%{oname}*


%changelog
* Tue Nov 22 2011 Götz Waschk <waschk@mandriva.org> 1.3.0-6mdv2012.0
+ Revision: 732428
- rebuild

* Fri Nov 19 2010 Funda Wang <fwang@mandriva.org> 1.3.0-5mdv2011.0
+ Revision: 598979
- rebuild for py2.7

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 1.3.0-4mdv2011.0
+ Revision: 442079
- rebuild

* Sat Jan 03 2009 Funda Wang <fwang@mandriva.org> 1.3.0-3mdv2009.1
+ Revision: 323539
- rebuild

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 1.3.0-2mdv2009.0
+ Revision: 269020
- rebuild early 2009.0 package (before pixel changes)

* Thu May 01 2008 Götz Waschk <waschk@mandriva.org> 1.3.0-1mdv2009.0
+ Revision: 199798
- fix buildrequires
- import python-clientcookie


