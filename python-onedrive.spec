%define		pypi_name	onedrive
Summary:	Python and command-line interface for Microsoft LiveConnect OneDrive REST API v5.0
Name:		python-%{pypi_name}
Version:	14.04.0
Release:	1
License:	WTFPL
Group:		Libraries/Python
Source0:	https://github.com/mk-fg/python-onedrive/archive/v%{version}/python-skydrive-%{version}.tar.gz
# Source0-md5:	c53d7e380816e5b198ddb46e8956d5d4
URL:		https://github.com/mk-fg/python-onedrive
BuildRequires:	python-devel
Suggests:	python-PyYAML
Suggests:	python-chardet
Suggests:	python-requests >= 0.14.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python and command-line interface for `OneDrive API (version 5.0)
(formerly known as SkyDrive).

This module allows to access data on Microsoft OneDrive cloud storage
from Python code, abstracting authentication, HTTP requests and
response processing to a simple Python methods.

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/skydrive-cli
%{py_sitescriptdir}/skydrive
%{py_sitescriptdir}/python_skydrive-%{version}-py*.egg-info
