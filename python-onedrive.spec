%define		pypi_name	onedrive
Summary:	Python and command-line interface for Microsoft LiveConnect OneDrive REST API v5.0
Name:		python-%{pypi_name}
Version:	14.04.3
Release:	1
License:	WTFPL
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/p/python-onedrive/%{name}-%{version}.tar.gz
# Source0-md5:	2da74c0fe68452bc84dd050617a33b3e
URL:		https://github.com/mk-fg/python-onedrive
BuildRequires:	python-devel
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
%doc README.txt
%attr(755,root,root) %{_bindir}/onedrive-cli
%{py_sitescriptdir}/onedrive
%{py_sitescriptdir}/python_onedrive-%{version}-py*.egg-info
