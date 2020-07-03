Summary: Pi-hole FTL binary
Name: pihole-ftl
Version: 5.0
Release: 3%{?dist}
License: GPL
URL: https://github.com/pi-hole/FTL/releases
%ifarch %{arm}
%define nsfile pihole-FTL-arm-linux-gnueabi
%endif
%ifarch aarch64
%define nsfile pihole-FTL-aarch64-linux-gnu
%endif
%ifarch x86_64
%define nsfile pihole-FTL-linux-x86_64
%endif
Source0: https://github.com/pi-hole/FTL/releases/download/v%{version}/%{nsfile}
Source1: https://raw.githubusercontent.com/pi-hole/FTL/master/LICENSE
Source2: ftl.service
Source3: pihole-FTL.conf
Source4: gravity.db.schema.sql

BuildRequires: systemd

%post
%systemd_post ftl.service

%preun
%systemd_preun ftl.service

%postun
%systemd_postun_with_restart ftl.service

# Disable debuginfo creation
%define debug_package %{nil}


%description
Pi-hole FTL binary

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/bin
mkdir -p %{buildroot}/etc/pihole
mkdir -p %{buildroot}/usr/lib/systemd/system/
mv %{SOURCE0} %{buildroot}/usr/bin/pihole-ftl
chmod 0755 %{buildroot}/usr/bin/pihole-ftl
mv %{SOURCE1} FTL-COPYING
mv %{SOURCE2} %{buildroot}/usr/lib/systemd/system/
mv %{SOURCE3} %{buildroot}/etc/pihole
mv %{SOURCE4} %{buildroot}/etc/pihole
echo %{pihole-ftl_release} > FTL-RELEASE


%files
%defattr(-,root,root)
/usr/bin/pihole-ftl
/usr/lib/systemd/system/ftl.service
/etc/pihole/gravity.db.schema.sql
%config(noreplace) /etc/pihole/pihole-FTL.conf
%dir /etc/pihole
%doc FTL-COPYING
%doc FTL-RELEASE

%changelog
* Thu Jul 02 2020 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 5.0-3
- ftl config: add MAXLOGAGE and MAXDBDAYS options

* Thu Jul 02 2020 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 5.0-2
- systemd unit: restart on failure

* Wed Jun 17 2020 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 5.0-1
- First release

