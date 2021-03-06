%define rev 20130124gitaa304d7

Name:           psi-plus-skins
Version:        0.16
Release:        0.1.%{rev}%{?dist}
Epoch:          2
BuildArch:      noarch
Summary:        Skins for Psi+

License:        Unknown
URL:            http://code.google.com/p/psi-dev/
Source0:        http://files.psi-plus.com/sources/%{name}-%{version}-%{rev}.tar.gz
Source1:        generate-tarball.sh

BuildRequires:  tar
Requires:       psi-plus-plugins >= 1:0.15-0.20.20110919git5117.R

%description
This package contains skins for Psi+.

%prep

%build

%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/psi-plus/
%{__tar} xzf %{SOURCE0} -C $RPM_BUILD_ROOT%{_datadir}/psi-plus/

%files
%{_datadir}/psi-plus/skins

%changelog
* Thu Jan 24 2013 Ivan Romanov <drizt@land.ru> - 2:0.16-0.1.20130124gitaa304d7.R
- updated to 20130124gitac60c0f
- dropped %%defattr
- source tarball moved to i-net

* Sun Oct 09 2011 Ivan Romanov <drizt@land.ru> - 0.15-0.1.20111009gita883f82.R
- Initial version of package
