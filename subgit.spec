%include	/usr/lib/rpm/macros.java
Summary:	Tool to migrate from subversion to git
Name:		subgit
Version:	3.1.1
Release:	0.1
# You may use SubGit for evaluation purposes without a registration as long as you like
# For production use registration is required.
# Import any project is Free
# http://www.subgit.com/pricing.html
License:	not redistributable
Group:		Development/Version Control
Source0:	http://old.subgit.com/download/%{name}-%{version}.zip
# NoSource0-md5:	39311874560161400360ad0fbd8c965b
NoSource:	0
URL:		http://www.subgit.com/
BuildRequires:	sed >= 4.0
BuildRequires:	unzip
Requires:	jre >= 1.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/%{name}

%description
SubGit is a tool for a smooth, stress-free SVN to Git migration.

Create writable Git mirror of a local or remote Subversion repository
and use both Subversion and Git as long as you like. You may also do a
fast one-time import from Subversion to Git or use SubGit within
Atlassian Stash.

%prep
%setup -q

%{__sed} -i -e '1 s,/bin/bash,/bin/sh,' bin/%{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_appdir}/bin,%{_bindir}}
install -p bin/subgit $RPM_BUILD_ROOT%{_appdir}/bin
ln -s %{_appdir}/bin/%{name}  $RPM_BUILD_ROOT%{_bindir}
cp -a lib $RPM_BUILD_ROOT%{_appdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt CHANGES.txt KNOWN_ISSUES.txt LICENSE.txt
%attr(755,root,root) %{_bindir}/subgit
%dir %{_appdir}
%dir %{_appdir}/bin
%attr(755,root,root) %{_appdir}/bin/subgit
%dir %{_appdir}/lib
%{_appdir}/lib/*.jar
%{_appdir}/lib/licenses
