%define oname ClientCookie
%define version 1.3.0
%define unmangled_version 1.3.0
%define unmangled_version 1.3.0
%define release %mkrel 5

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
Url: http://wwwsearch.sourceforge.net/ClientCookie/

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
