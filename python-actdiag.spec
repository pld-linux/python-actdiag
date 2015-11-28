%define 	module	actdiag
Summary:	actdiag generate activity-diagram image file from spec-text file
Name:		python-%{module}
Version:	0.3.3
Release:	1
License:	Apache v2.0
Group:		Development/Languages
URL:		http://blockdiag.com/en/actdiag/index.html
Source0:	http://pypi.python.org/packages/source/a/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	9fe115a937539c43cf9d16a5d79e20d6
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	sed >= 4.0
Requires:	python-blockdiag >= 1.1.2
Requires:	python-funcparserlib >= 0.3.4
Requires:	python-modules >= 2.4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
actdiag generate activity-diagram image file from spec-text file.

Features:
- Generate activity-diagram from dot like text (basic feature).
- Multilingualization for node-label (utf-8 only).

%prep
%setup -q -n %{module}-%{version}
%{__sed} -i -e 's/^from ez_setup/#from ez_setup/' setup.py
%{__sed} -i -e 's/^use_setuptools()/#use_setuptools()/' setup.py

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install \
	--root $RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/%{module}/tests
%{__rm} $RPM_BUILD_ROOT%{py_sitescriptdir}/%{module}_sphinxhelper.py[co]

install -d $RPM_BUILD_ROOT%{_mandir}/man1
cp -p %{module}.1 $RPM_BUILD_ROOT%{_mandir}/man1

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{module}
%{_mandir}/man1/%{module}.1*
%dir %{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}/*.py[co]
%dir %{py_sitescriptdir}/%{module}/plugins
%{py_sitescriptdir}/%{module}/plugins/*.py[co]
%dir %{py_sitescriptdir}/%{module}/utils
%{py_sitescriptdir}/%{module}/utils/*.py[co]
%dir %{py_sitescriptdir}/%{module}/utils/rst
%{py_sitescriptdir}/%{module}/utils/rst/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/%{module}-%{version}-*.egg-info
%endif
