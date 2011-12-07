Name:       ibus-table
Version:    1.2.0.20100111
Release:    4%{?dist}
Summary:    Table engine for IBus
License:    LGPLv2+
Group:      System Environment/Libraries
URL:        http://code.google.com/p/ibus/
Source0:    http://ibus.googlecode.com/files/%{name}-%{version}.tar.gz
Patch0:     ibus-table-1.2.0.20100111-2-equal-sign.patch
Patch1:     ibus-table-1.2.0.20100111-3-non-exec-script.patch

Requires:       ibus >= 1.2
BuildRequires:  ibus-devel >= 1.2

BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:  noarch

%description
The package contains Table engine for IBus.

%package additional
Summary:    Additional tables for general table engine of IBus
Group:      System Environment/Libraries
Requires:   %{name} = %{version}-%{release}

%description additional
This package contains additional tables for Ibus-Table.

%package -n %{name}-devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}, pkgconfig

%description -n %{name}-devel
Headers and other files needed to develop applications using the %{name}
 library.

%prep
%setup -q
%patch0 -p1 -b .2-equal-sign
%patch1 -p1 -b .3-non-exec-script

%build
%configure --disable-static \
    --prefix=%{_prefix} \
    --enable-additional
%__make %{?_smp_mflags}

%install
%__rm -rf $RPM_BUILD_ROOT
%__make DESTDIR=${RPM_BUILD_ROOT} NO_INDEX=true install pkgconfigdir=%{_datadir}/pkgconfig

%find_lang %{name}

%clean
%__rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%post additional
ibus-table-createdb -i -n %{_datadir}/ibus-table/tables/compose.db
ibus-table-createdb -i -n %{_datadir}/ibus-table/tables/latex.db

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING README
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/engine
%dir %{_datadir}/%{name}/tables
%dir %{_datadir}/%{name}/icons
%dir %{_datadir}/%{name}/data
%{_datadir}/ibus/component/table.xml
%{_datadir}/%{name}/data/pinyin_table.txt.bz2
%{_datadir}/%{name}/engine/factory.py
%{_datadir}/%{name}/engine/factory.pyc
%{_datadir}/%{name}/engine/factory.pyo
%{_datadir}/%{name}/engine/main.py
%{_datadir}/%{name}/engine/main.pyc
%{_datadir}/%{name}/engine/main.pyo
%{_datadir}/%{name}/engine/tabcreatedb.py
%{_datadir}/%{name}/engine/tabcreatedb.pyc
%{_datadir}/%{name}/engine/tabcreatedb.pyo
%{_datadir}/%{name}/engine/tabdict.py
%{_datadir}/%{name}/engine/tabdict.pyc
%{_datadir}/%{name}/engine/tabdict.pyo
%{_datadir}/%{name}/engine/table.py
%{_datadir}/%{name}/engine/table.pyc
%{_datadir}/%{name}/engine/table.pyo
%{_datadir}/%{name}/engine/tabsqlitedb.py
%{_datadir}/%{name}/engine/tabsqlitedb.pyc
%{_datadir}/%{name}/engine/tabsqlitedb.pyo
%{_datadir}/%{name}/icons/acommit.svg
%{_datadir}/%{name}/icons/cb-mode.svg
%{_datadir}/%{name}/icons/chinese.svg
%{_datadir}/%{name}/icons/ibus-table.svg
%{_datadir}/%{name}/icons/english.svg
%{_datadir}/%{name}/icons/full-letter.svg
%{_datadir}/%{name}/icons/full-punct.svg
%{_datadir}/%{name}/icons/half-letter.svg
%{_datadir}/%{name}/icons/half-punct.svg
%{_datadir}/%{name}/icons/ncommit.svg
%{_datadir}/%{name}/icons/onechar.svg
%{_datadir}/%{name}/icons/phrase.svg
%{_datadir}/%{name}/icons/py-mode.svg
%{_datadir}/%{name}/icons/sc-mode.svg
%{_datadir}/%{name}/icons/scb-mode.svg
%{_datadir}/%{name}/icons/tab-mode.svg
%{_datadir}/%{name}/icons/tc-mode.svg
%{_datadir}/%{name}/icons/tcb-mode.svg
%{_libexecdir}/ibus-engine-table
%{_bindir}/%{name}-createdb

%files additional
%defattr(-,root,root,-)
%{_datadir}/%{name}/tables/template.txt
%{_datadir}/%{name}/tables/compose.db
%{_datadir}/%{name}/tables/latex.db
%{_datadir}/%{name}/icons/compose.svg
%{_datadir}/%{name}/icons/latex.svg

%files devel
%defattr(-, root, root, -)
%{_datadir}/pkgconfig/%{name}.pc

%changelog
* Thu Feb 04 2010 Caius 'kaio' Chance <cchance at redhat.com> - 1.2.0.20100111-4
- Resolves: rhbz#559799.
- Shorten description under 80 characters.

* Fri Jan 29 2010 Caius 'kaio' Chance <cchance at redhat.com> - 1.2.0.20100111-3
- Resolves: rhbz#559799.
- Split devel file into devel package.
- Fix non-executable-script of tabcreatedb.py.

* Fri Jan 29 2010 Caius 'kaio' Chance <cchance at redhat.com> - 1.2.0.20100111-2
- Resolves: rhbz#559799.
- Added resolution to deal with '=' as combination key.

* Thu Jan 28 2010 Caius 'kaio' Chance <cchance at redhat.com> - 1.2.0.20100111-1
- Resolves: rhbz#559799.
- Update source tarball, also sync version number to tarball version.

* Thu Jan 28 2010 Caius 'kaio' Chance <cchance at redhat.com> - 1.2.0.20091014-5
- Resolves: rhbz#559457.
- Rebuilt.

* Thu Jan 28 2010 Caius 'kaio' Chance <cchance at redhat.com> - 1.2.0.20091014-4
- Resolves: rhbz#559457.
- Non exec scripts shouldn't have !/usr/bin/python on the first line.

* Wed Nov 11 2009 Caius 'kaio' Chance <k at kaio.me> - 1.2.0.20091014-3.fc12
- rebuilt

* Wed Nov 11 2009 Caius 'kaio' Chance <k at kaio.me> - 1.2.0.20091014-2.fc12
- Update to upstream source.
- Fix crashing caused by speedmeter.

* Fri Oct 23 2009 Caius 'kaio' Chance <k at kaio.me> - 1.2.0.20091014-1.fc12
- Regression of crashing: rollback to 20090902.

* Fri Sep 04 2009 Caius 'kaio' Chance <k at kaio.me> - 1.2.0.20090912-1.fc12
- Upgraded to upstream source.

* Fri Sep 04 2009 Caius 'kaio' Chance <k at kaio.me> - 1.2.0.20090904-1.fc12
- Updated source with additional tables separated.

* Thu Sep 03 2009 Caius 'kaio' Chance <k at kaio.me> - 1.2.0.20090902-2.fc12
- Rebuilt.

* Wed Sep 02 2009 Caius 'kaio' Chance <k at kaio.me> - 1.2.0.20090902-1.fc12
- Updated source.

* Tue Aug 04 2009 Caius 'kaio' Chance <k at kaio.me> - 1.2.0.20090804-1.fc12
- Cleaned up unused dcommit contents.

* Tue Aug 03 2009 Caius 'kaio' Chance <k at kaio.me> - 1.2.0.20090803-1.fc12
- Updated to upstream.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0.20090625-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 01 2009 Caius 'kaio' Chance <k at kaio.me> - 1.2.0.20090625-2.fc12
- Rebuilt.

* Wed Jul 01 2009 Caius 'kaio' Chance <k at kaio.me> - 1.2.0.20090625-1.fc12
- Updated source from upstream, which released for IBus 1.2 and so on.

* Wed May 27 2009 Caius 'kaio' Chance <cchance@redhat.com> - 1.1.0.20090527-1.fc12
- Updated source from upstream, which with candidate order fix.

* Mon Mar 16 2009 Caius Chance <cchance@redhat.com> - 1.1.0.20090316-1.fc11
- Resolves: rhbz#490396
- Updated source tarball.
- Disabled speedmeter until config option is implemented.

* Fri Mar  6 2009 Jens Petersen <petersen@redhat.com> - 1.1.0.20090220-5
- make pkgconfig noarch with ibus-table-pkgconfig-noarch.patch
- fix license field: actually LGPL
- drop gettext-devel BR
- require ibus > 1.1.0

* Mon Mar 02 2009 Caius Chance <cchance@redhat.com> - 1.1.0.20090220-4.fc11
- Rebuilt.

* Mon Mar 02 2009 Caius Chance <cchance@redhat.com> - 1.1.0.20090220-3.fc11
- Rebuilt.

* Mon Mar 02 2009 Caius Chance <cchance@redhat.com> - 1.1.0.20090220-2.fc11
- Rebuilt.

* Mon Mar 02 2009 Caius Chance <cchance@redhat.com> - 1.1.0.20090220-1.fc11
- Resolves: rhbz#484650
- Updated to latest upstream release.
- Splitted chinese input methods into modules.

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1.20081014-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 04 2009 Caius Chance <cchance@redhat.com> - 0.1.1.20081014-4
- Resolves: rhbz#466430 rhbz#466844
- Added wildcard features.
- Added preedit clearance on refocus.

* Mon Dec 01 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.1.1.20081014-3
- Rebuild for Python 2.6

* Mon Dec 1 2008 Peng Huang <shawn.p.huang@gmail.com> - 0.1.1.20081014-2
- Modified spec file to own all directories created by ibus-table.

* Fri Oct 14 2008 Peng Huang <shawn.p.huang@gmail.com> - 0.1.1.20081014-1
- Update to 0.1.1.20081014.

* Mon Sep 01 2008 Peng Huang <shawn.p.huang@gmail.com> - 0.1.1.20080901-1
- Update to 0.1.1.20080901.

* Wed Aug 19 2008 Yu Yuwei <acevery@gmail.com> - 0.1.1.20080829-1
- The first version.
